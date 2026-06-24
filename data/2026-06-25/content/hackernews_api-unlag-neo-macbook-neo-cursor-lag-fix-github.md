---
title: 'Unlag Neo: Macbook Neo Cursor lag "fix" · GitHub'
url: https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf
site_name: hackernews_api
content_file: hackernews_api-unlag-neo-macbook-neo-cursor-lag-fix-github
fetched_at: '2026-06-25T05:55:20.555720'
original_url: https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf
author: retroplasma
date: '2026-06-24'
description: 'Unlag Neo: Macbook Neo Cursor lag "fix". GitHub Gist: instantly share code, notes, and snippets.'
tags:
- hackernews
- trending
---

Instantly share code, notes, and snippets.

# retroplasma/README.md

 Last active
 
June 24, 2026 17:49

 

Show Gist options

 

* Download ZIP

 

 

* Star15(15)You must be signed in to star a gist
* Fork0(0)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf to your computer and use it in GitHub Desktop.

 

Embed

# Select an option

 

* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found

 

 
 
Learn more about clone URLs

 

 

 Clone this repository at &lt;script src=&quot;https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf.js&quot;&gt;&lt;/script&gt;

 

 

Save retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf to your computer and use it in GitHub Desktop.

Download ZIP

 Unlag Neo: Macbook Neo Cursor lag "fix"
 

 

Raw

 README.md
 

# Unlag Neo: A "fix" for the cursor lag on Macbook Neo

Macbook Neo (I'm on macOS Tahoe 26.5.1) cursor is lagging when the cursor is near the screen's edges or when it enters a Terminal window.[1][2][3][4][5]

[Click here for more info and background]

### Why is it lagging?

I don't know. But at the moment when it lags the system switches from hardware cursor to software cursor (CGCursorIsDrawnInFramebuffer()goes from0to1) so maybe that transition is stalled somehow on Macbook Neo.
Maybe on the screen's edges half of the mouse is rendered and in the Terminal there is some other graphics stuff happening, so that's why macOS wants to use SW cursor there, but idk. For some reason, HW cursor is only used after ~17 seconds after the screen was locked. Before that, there is no lag.

### Proper fix:

Either fix the lag directly (hope Apple does it) or maybe forcing to always use SW cursor would help as a intermediate step. To force SW cursor directly we could reverse engineer WindowServer but that probably implies turning SIP off and stuff. Or maybe not. And maybe HW/SW cursor is just a correlation. We could also look what happens ~17 seconds after Mac is unlocked.

### Other ok "fix" for now:

You can also turn on macOS Color Filter (e.g. Blue/Yellow filter) to low setting, but this changes the colors a bit and doesn't seem to help if Night Shift is on at the same time. Also the mouse cursor size can be changed, but a small change doesn't work; it has to be significantly bigger to trigger the fix.
But to keep the colors and cursor ok, we can also do a Screen Recording. However with screen recording there is an indicdator () on the top right of the screen. Maybe it can be disabled with SIP off but I haven't looked.

Essentially anything that forces the compositor(?) to do SW cursor (or whatever else) will do. No lag anymore.

### Other idea:

Find out what's special about the Terminal window and create an app that does the same thing and overlays its window over everything.

Anyway, I chose Screen Recording.

### My favorite "fix" right now: Screen Recording

For me, the Screen Recording solution is the least annoying one. The indicator () is small enough and we can turn off screen recording when a fullscreen video is playing (where the indicator would be annoying otherwise imho). Obviously, such a fix would invalidate the purpose of that indicator, but I think there are two kinds of indicators. There is a larger one also, which (I think) app store apps have, so I think we are fine-ish.

The cursor stops lagging.

### It doesn't need much CPU/GPU:

Record 1 pixel every 10 seconds (to/dev/nullbasically, no SSD write)

### Ok how to do it:

There is a script (create_unlag_neo_app.sh) below in this Gist. The script creates an.appwhich can be launched (no need for Dev Account or Xcode etc.).

The script can be used like this (Terminal):

chmod +x create_unlag_neo_app.sh
./create_unlag_neo_app.sh

#
 -> creates "Unlag Neo.app"

App that the script created:

PutUnlag Neo.appsomewhere. In/Applicationsor something.
Run it and give it the permission it wants.

In the menu bar () you can turn it off and also try the "Pause in Fullscreen" feature if you want, which does an OK job I think to hide the indicator. I tried with VLC and YouTube and a few apps.

[[Click here for Debug info]]

### Debug

If you want to hackcreate_unlag_neo_app.shand rebuild the app multiple times, macOS permission settings UI can reset and behave a bit weirdly. You can try to change"Unlag Neo"to something else in the script, or drag the app icon into permissions settings manually, or try to delete"~/Library/Preferences/Unlag Neo.plist"orkillall cfprefsdor just use Xcode.

 

Raw

 create_unlag_neo_app.sh
 

#!
/bin/bash

set
 -Efeuxo pipefail

APP=
"
Unlag Neo
"

DISPLAY_NAME=
"
Unlag Neo
"

if
 [ 
-e
 
"
${APP}
.app
"
 ]
;
 
then

 
echo
 
"
Error: 
${APP}
.app exists already
"

 
exit
 1

fi

mkdir -vp 
"
${APP}
.app/Contents/MacOS
"
 
"
${APP}
.app/Contents/Resources
"

PATH=
"
$PATH
:/usr/libexec
"

swiftc - -o 
"
${APP}
.app/Contents/MacOS/
${APP}
"
 
<<
'
SWIFT
'

import Foundation

import AppKit

import CoreGraphics

import CoreMedia

import ServiceManagement

import ApplicationServices

@preconcurrency import ScreenCaptureKit

struct CaptureError: Error, CustomStringConvertible {

 let description: String

 init(_ description: String) { self.description = description }

}

@MainActor var showedPermissionAlert = false

@MainActor var showedAccessibilityAlert = false

@MainActor

func relaunchUnlag() {

 let isApp = Bundle.main.bundlePath.hasSuffix(".app")

 let target = isApp ? Bundle.main.bundlePath : (Bundle.main.executablePath ?? Bundle.main.bundlePath)

 let p = Process()

 p.executableURL = URL(fileURLWithPath: "/bin/sh")

 p.arguments = ["-c", isApp ? "sleep 0.5; /usr/bin/open \"$1\"" : "sleep 0.5; \"$1\" >/dev/null 2>&1 &", "sh", target]

 try? p.run()

 NSApp.terminate(nil)

}

@MainActor

func openScreenRecordingSettings() {

 NSWorkspace.shared.open(URL(string: "x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture")!)

}

@MainActor

func openAccessibilitySettings() {

 NSWorkspace.shared.open(URL(string: "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility")!)

}

@MainActor

func showPermissionAlert() {

 NSApp.activate(ignoringOtherApps: true)

 let a = NSAlert()

 a.alertStyle = .warning

 a.messageText = "Screen Recording Permission Needed"

 a.informativeText = "Give Screen Recording permission in System Settings, then restart Unlag Neo."

 a.addButton(withTitle: "Open Settings")

 a.addButton(withTitle: "Restart Unlag Neo")

 a.addButton(withTitle: "Quit Unlag Neo")

 switch a.runModal() {

 case .alertFirstButtonReturn:

 openScreenRecordingSettings()

 let b = NSAlert()

 b.alertStyle = .informational

 b.messageText = "Restart Unlag Neo After Permission"

 b.informativeText = "After enabling Screen Recording permission, restart Unlag Neo."

 b.addButton(withTitle: "Restart Unlag Neo")

 b.addButton(withTitle: "Quit Unlag Neo")

 if b.runModal() == .alertFirstButtonReturn {

 relaunchUnlag()

 } else {

 NSApp.terminate(nil)

 }

 case .alertSecondButtonReturn:

 relaunchUnlag()

 default:

 NSApp.terminate(nil)

 }

}

@MainActor

func showAccessibilityAlert() {

 guard !showedAccessibilityAlert else { return }

 showedAccessibilityAlert = true

 NSApp.activate(ignoringOtherApps: true)

 let a = NSAlert()

 a.alertStyle = .warning

 a.messageText = "Accessibility Permission Needed"

 a.informativeText = "Give Accessibility permission in System Settings, then restart Unlag Neo."

 a.addButton(withTitle: "Open Settings")

 a.addButton(withTitle: "Restart Unlag Neo")

 a.addButton(withTitle: "Quit Unlag Neo")

 switch a.runModal() {

 case .alertFirstButtonReturn:

 openAccessibilitySettings()

 let b = NSAlert()

 b.alertStyle = .informational

 b.messageText = "Restart Unlag Neo After Permission"

 b.informativeText = "After enabling Accessibility permission, restart Unlag Neo."

 b.addButton(withTitle: "Restart Unlag Neo")

 b.addButton(withTitle: "Quit Unlag Neo")

 if b.runModal() == .alertFirstButtonReturn {

 relaunchUnlag()

 } else {

 NSApp.terminate(nil)

 }

 case .alertSecondButtonReturn:

 relaunchUnlag()

 default:

 NSApp.terminate(nil)

 }

}

@MainActor

func requireScreenRecordingPermission() throws {

 guard !CGPreflightScreenCaptureAccess() else { return }

 _ = CGRequestScreenCaptureAccess()

 if !showedPermissionAlert {

 showedPermissionAlert = true

 showPermissionAlert()

 }

 throw CaptureError("Missing Screen Recording permission.")

}

func axCopy(_ element: AXUIElement, _ attr: String) -> AnyObject? {

 var value: CFTypeRef?

 return AXUIElementCopyAttributeValue(element, attr as CFString, &value) == .success ? value : nil

}

func axBool(_ element: AXUIElement, _ attr: String) -> Bool {

 (axCopy(element, attr) as? NSNumber)?.boolValue ?? false

}

func axValue(_ element: AXUIElement, _ attr: String, _ type: AXValueType) -> AXValue? {

 guard let v = axCopy(element, attr) else { return nil }

 let axv = v as! AXValue

 return AXValueGetType(axv) == type ? axv : nil

}

func axRect(_ element: AXUIElement) -> CGRect? {

 guard let p = axValue(element, kAXPositionAttribute, .cgPoint),

 let s = axValue(element, kAXSizeAttribute, .cgSize)

 else { return nil }

 var point = CGPoint.zero

 var size = CGSize.zero

 guard AXValueGetValue(p, .cgPoint, &point),

 AXValueGetValue(s, .cgSize, &size)

 else { return nil }

 return CGRect(origin: point, size: size)

}

func focusedOrMainWindow(_ app: AXUIElement) -> AXUIElement? {

 if let w = axCopy(app, kAXFocusedWindowAttribute) {

 return (w as! AXUIElement)

 }

 if let w = axCopy(app, kAXMainWindowAttribute) {

 return (w as! AXUIElement)

 }

 return nil

}

func axWindows(_ app: AXUIElement) -> [AXUIElement] {

 guard let xs = axCopy(app, kAXWindowsAttribute) as? [AnyObject] else { return [] }

 return xs.map { $0 as! AXUIElement }

}

func displayRects() -> [CGRect] {

 var count: UInt32 = 0

 CGGetActiveDisplayList(0, nil, &count)

 var ids = [CGDirectDisplayID](repeating: 0, count: Int(count))

 CGGetActiveDisplayList(count, &ids, &count)

 return ids.prefix(Int(count)).map { CGDisplayBounds($0) }

}

func fillsDisplay(_ rect: CGRect, _ display: CGRect) -> Bool {

 let t: CGFloat = 8

 let i = rect.intersection(display)

 return i.width >= display.width - t && i.height >= display.height - t

}

func windowLooksFullscreen(_ window: AXUIElement, _ displays: [CGRect]) -> Bool {

 if axBool(window, "AXFullScreen") {

 return true

 }

 guard let rect = axRect(window) else { return false }

 return displays.contains { fillsDisplay(rect, $0) }

}

func cgFullscreenWindowVisible() -> Bool {

 guard let app = NSWorkspace.shared.frontmostApplication else { return false }

 guard app.bundleIdentifier != "com.apple.finder" else { return false }

 let pid = Int(app.processIdentifier)

 let selfPid = Int(ProcessInfo.processInfo.processIdentifier)

 let displays = displayRects()

 guard pid != selfPid,

 let windows = CGWindowListCopyWindowInfo([.optionOnScreenOnly, .excludeDesktopElements], kCGNullWindowID) as? [[String: Any]]

 else {

 return false

 }

 for w in windows {

 guard let owner = (w[kCGWindowOwnerPID as String] as? NSNumber)?.intValue,

 owner == pid,

 let layer = (w[kCGWindowLayer as String] as? NSNumber)?.intValue,

 layer == 0,

 let alpha = (w[kCGWindowAlpha as String] as? NSNumber)?.doubleValue,

 alpha > 0,

 let bounds = w[kCGWindowBounds as String] as? NSDictionary,

 let rect = CGRect(dictionaryRepresentation: bounds as CFDictionary)

 else { continue }

 if displays.contains(where: { fillsDisplay(rect, $0) }) {

 return true

 }

 }

 return false

}

func hasFullscreenWindowVisible() -> Bool {

 guard NSWorkspace.shared.frontmostApplication?.bundleIdentifier != "com.apple.finder" else {

 return false

 }

 let displays = displayRects()

 if AXIsProcessTrusted(),

 let app = NSWorkspace.shared.frontmostApplication,

 app.processIdentifier != ProcessInfo.processInfo.processIdentifier {

 let axApp = AXUIElementCreateApplication(app.processIdentifier)

 var windows = axWindows(axApp)

 if let w = focusedOrMainWindow(axApp) {

 windows.insert(w, at: 0)

 }

 for w in windows {

 if windowLooksFullscreen(w, displays) {

 return true

 }

 }

 }

 return cgFullscreenWindowVisible()

}

func statusIcon() -> NSImage {

 let size = NSSize(width: 22, height: 22)

 let img = NSImage(size: size)

 img.lockFocus()

 NSColor.labelColor.setStroke()

 let circle = NSBezierPath(ovalIn: NSRect(x: 4, y: 4, width: 14, height: 14))

 circle.lineWidth = 1.5

 circle.stroke()

 let attrs: [NSAttributedString.Key: Any] = [

 .font: NSFont.boldSystemFont(ofSize: 7),

 .foregroundColor: NSColor.labelColor

 ]

 let s = NSString(string: "UN")

 let textSize = s.size(withAttributes: attrs)

 s.draw(

 at: NSPoint(

 x: (size.width - textSize.width) / 2,

 y: (size.height - textSize.height) / 2 + 0

 ),

 withAttributes: attrs

 )

 img.unlockFocus()

 img.isTemplate = true

 return img

}

func axCallback(_ observer: AXObserver, _ element: AXUIElement, _ notification: CFString, _ refcon: UnsafeMutableRawPointer?) {

 guard let refcon else { return }

 let app = Unmanaged<AppDelegate>.fromOpaque(refcon).takeUnretainedValue()

 DispatchQueue.main.async {

 app.axEvent()

 }

}

final class NullStreamOutput: NSObject, SCStreamOutput {

 private(set) var frameCount = 0

 private var printed = false

 func stream(_ stream: SCStream, didOutputSampleBuffer sampleBuffer: CMSampleBuffer, of type: SCStreamOutputType) {

 guard type == .screen, sampleBuffer.isValid,

 let a = CMSampleBufferGetSampleAttachmentsArray(sampleBuffer, createIfNecessary: false) as? [[SCStreamFrameInfo: Any]],

 let raw = a.first?[SCStreamFrameInfo.status] as? Int,

 SCFrameStatus(rawValue: raw) == .complete

 else { return }

 frameCount += 1

 guard !printed else { return }

 printed = true

 if let b = CMSampleBufferGetImageBuffer(sampleBuffer) {

 print("Receiving \(CVPixelBufferGetWidth(b))x\(CVPixelBufferGetHeight(b)) frames every 10 seconds and dropping them.")

 } else {

 print("Receiving frames every 10 seconds and dropping them.")

 }

 }

}

actor Capture {

 private var stream: SCStream?

 private var output: NullStreamOutput?

 private var starting = false

 private let queue = DispatchQueue(label: "u.capture.samples")

 func start() async {

 guard stream == nil, !starting else { return }

 starting = true

 defer { starting = false }

 do {

 try await MainActor.run { try requireScreenRecordingPermission() }

 let id = CGMainDisplayID()

 let content = try await SCShareableContent.current

 guard let display = content.displays.first(where: { $0.displayID == id }) else {

 throw CaptureError("Could not find the main display.")

 }

 let c = SCStreamConfiguration()

 c.sourceRect = CGRect(x: 0, y: 0, width: 1, height: 1)

 c.width = 1

 c.height = 1

 c.minimumFrameInterval = CMTime(value: 10, timescale: 1)

 c.queueDepth = 4

 c.showsCursor = true

 c.capturesAudio = false

 c.pixelFormat = kCVPixelFormatType_32BGRA

 let o = NullStreamOutput()

 let s = SCStream(filter: SCContentFilter(display: display, excludingWindows: []), configuration: c, delegate: nil)

 try s.addStreamOutput(o, type: .screen, sampleHandlerQueue: queue)

 output = o

 stream = s

 print("Starting 1x1 null screen capture with cursor enabled.")

 try await s.startCapture()

 print("Running. One frame every 10 seconds.")

 } catch {

 stream = nil

 output = nil

 print("Error:", error)

 }

 }

 func stop() async {

 guard let s = stream else { return }

 let n = output?.frameCount ?? 0

 stream = nil

 output = nil

 do {

 try await s.stopCapture()

 print("Stopped. Dropped \(n) frames.")

 } catch {

 print("Stop error:", error)

 }

 }

 func restart() async {

 print("Restarting capture.")

 await stop()

 await start()

 }

}

final class AppDelegate: NSObject, NSApplicationDelegate, NSMenuDelegate {

 private var item: NSStatusItem!

 private var enabledSwitch: NSSwitch!

 private var fullscreenSwitch: NSSwitch!

 private var loginSwitch: NSSwitch!

 private var isEnabled = true

 private var pauseInFullscreen = UserDefaults.standard.bool(forKey: "pauseInFullscreen")

 private var captureWanted: Bool?

 private var pendingSecondApply = false

 private var pendingWakeDebounce = false

 private var fullscreenDebounce: DispatchWorkItem?

 private var axObserver: AXObserver?

 private var axApp: AXUIElement?

 private var axObservedWindows: [AXUIElement] = []

 private let capture = Capture()

 func applicationWillFinishLaunching(_ notification: Notification) {

 _ = NSApp.setActivationPolicy(.accessory)

 }

 func applicationDidFinishLaunching(_ notification: Notification) {

 item = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)

 item.button?.image = statusIcon()

 item.button?.imagePosition = .imageOnly

 let menu = NSMenu()

 menu.delegate = self

 let enabledRow = switchRow(title: "Unlag Neo Enabled", state: .on, action: #selector(toggleEnabled))

 enabledSwitch = enabledRow.1

 menu.addItem(enabledRow.0)

 let fullscreenRow = switchRow(title: "Pause in Fullscreen", state: pauseInFullscreen ? .on : .off, action: #selector(toggleFullscreenPause))

 fullscreenSwitch = fullscreenRow.1

 menu.addItem(fullscreenRow.0)

 let loginRow = switchRow(title: "Launch at Login", state: SMAppService.mainApp.status == .enabled ? .on : .off, action: #selector(toggleLoginItem))

 loginSwitch = loginRow.1

 menu.addItem(loginRow.0)

 menu.addItem(.separator())

 let exit = NSMenuItem(title: "Exit", action: #selector(exit), keyEquivalent: "q")

 exit.target = self

 menu.addItem(exit)

 item.menu = menu

 let wc = NSWorkspace.shared.notificationCenter

 wc.addObserver(self, selector: #selector(wake), name: NSWorkspace.didWakeNotification, object: nil)

 wc.addObserver(self, selector: #selector(frontAppChanged), name: NSWorkspace.activeSpaceDidChangeNotification, object: nil)

 wc.addObserver(self, selector: #selector(frontAppChanged), name: NSWorkspace.didActivateApplicationNotification, object: nil)

 NotificationCenter.default.addObserver(self, selector: #selector(frontAppChanged), name: NSApplication.didChangeScreenParametersNotification, object: nil)

 Task { await capture.start() }

 DispatchQueue.main.async {

 self.captureWanted = true

 self.setupAXObserver()

 self.applyCaptureState(force: true)

 self.applyAgainNextMainLoop()

 }

 }

 private func switchRow(title: String, state: NSControl.StateValue, action: Selector) -> (NSMenuItem, NSSwitch) {

 let item = NSMenuItem()

 let view = NSView(frame: NSRect(x: 0, y: 0, width: 250, height: 42))

 let label = NSTextField(labelWithString: title)

 let sw = NSSwitch()

 label.translatesAutoresizingMaskIntoConstraints = false

 sw.translatesAutoresizingMaskIntoConstraints = false

 label.font = NSFont.menuFont(ofSize: 0)

 sw.state = state

 sw.target = self

 sw.action = action

 view.addSubview(label)

 view.addSubview(sw)

 NSLayoutConstraint.activate([

 label.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16),

 label.centerYAnchor.constraint(equalTo: view.centerYAnchor),

 sw.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16),

 sw.centerYAnchor.constraint(equalTo: view.centerYAnchor),

 label.trailingAnchor.constraint(lessThanOrEqualTo: sw.leadingAnchor, constant: -12)

 ])

 item.view = view

 return (item, sw)

 }

 private func cleanupAXObserver() {

 if let o = axObserver {

 CFRunLoopRemoveSource(CFRunLoopGetMain(), AXObserverGetRunLoopSource(o), .defaultMode)

 }

 axObserver = nil

 axApp = nil

 axObservedWindows = []

 }

 private func addAX(_ observer: AXObserver, _ element: AXUIElement, _ name: String) {

 _ = AXObserverAddNotification(observer, element, name as CFString, Unmanaged.passUnretained(self).toOpaque())

 }

 private func attachAXWindows() {

 guard let observer = axObserver, let app = axApp else { return }

 var windows = axWindows(app)

 if let w = focusedOrMainWindow(app) {

 windows.insert(w, at: 0)

 }

 axObservedWindows = windows

 for w in windows {

 addAX(observer, w, kAXMovedNotification)

 addAX(observer, w, kAXResizedNotification)

 addAX(observer, w, kAXUIElementDestroyedNotification)

 addAX(observer, w, "AXFullScreenChanged")

 }

 }

 private func setupAXObserver() {

 cleanupAXObserver()

 guard pauseInFullscreen else { return }

 let opts = [kAXTrustedCheckOptionPrompt.takeUnretainedValue() as String: true] as CFDictionary

 guard AXIsProcessTrustedWithOptions(opts) else {

 Task { await MainActor.run { showAccessibilityAlert() } }

 return

 }

 guard let app = NSWorkspace.shared.frontmostApplication,

 app.processIdentifier != ProcessInfo.processInfo.processIdentifier,

 app.bundleIdentifier != "com.apple.finder"

 else { return }

 var observer: AXObserver?

 guard AXObserverCreate(app.processIdentifier, axCallback, &observer) == .success, let observer else { return }

 axObserver = observer

 axApp = AXUIElementCreateApplication(app.processIdentifier)

 if let axApp {

 addAX(observer, axApp, kAXFocusedWindowChangedNotification)

 addAX(observer, axApp, kAXMainWindowChangedNotification)

 addAX(observer, axApp, kAXWindowCreatedNotification)

 }

 attachAXWindows()

 CFRunLoopAddSource(CFRunLoopGetMain(), AXObserverGetRunLoopSource(observer), .defaultMode)

 }

 private func shouldCapture() -> Bool {

 isEnabled && !(pauseInFullscreen && hasFullscreenWindowVisible())

 }

 private func applyCaptureState(restart: Bool = false, force: Bool = false) {

 let run = shouldCapture()

 if !force, !restart, captureWanted == run {

 return

 }

 captureWanted = run

 Task {

 if run {

 if restart {

 await capture.restart()

 } else {

 await capture.start()

 }

 } else {

 await capture.stop()

 }

 }

 }

 private func applyAgainNextMainLoop() {

 guard !pendingSecondApply else { return }

 pendingSecondApply = true

 DispatchQueue.main.async { [weak self] in

 guard let self else { return }

 self.pendingSecondApply = false

 self.attachAXWindows()

 self.applyCaptureState(force: true)

 }

 }

 private func applyAfterWakeDebounce() {

 guard !pendingWakeDebounce else { return }

 pendingWakeDebounce = true

 DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) { [weak self] in

 guard let self else { return }

 self.pendingWakeDebounce = false

 self.setupAXObserver()

 self.applyCaptureState(restart: true, force: true)

 self.applyAgainNextMainLoop()

 }

 }

 private func applyAfterFullscreenDebounce() {

 fullscreenDebounce?.cancel()

 let work = DispatchWorkItem { [weak self] in

 guard let self else { return }

 self.fullscreenDebounce = nil

 self.setupAXObserver()

 self.applyCaptureState(force: true)

 self.applyAgainNextMainLoop()

 }

 fullscreenDebounce = work

 DispatchQueue.main.asyncAfter(deadline: .now() + 1.0, execute: work)

 }

 func menuWillOpen(_ menu: NSMenu) {

 enabledSwitch.state = isEnabled ? .on : .off

 fullscreenSwitch.state = pauseInFullscreen ? .on : .off

 loginSwitch.state = SMAppService.mainApp.status == .enabled ? .on : .off

 }

 @objc private func toggleEnabled(_ sender: NSSwitch) {

 isEnabled = sender.state == .on

 applyCaptureState()

 }

 @objc private func toggleFullscreenPause(_ sender: NSSwitch) {

 pauseInFullscreen = sender.state == .on

 UserDefaults.standard.set(pauseInFullscreen, forKey: "pauseInFullscreen")

 setupAXObserver()

 applyCaptureState()

 applyAgainNextMainLoop()

 }

 @objc private func toggleLoginItem(_ sender: NSSwitch) {

 do {

 if sender.state == .on {

 try SMAppService.mainApp.register()

 } else {

 try SMAppService.mainApp.unregister()

 }

 sender.state = SMAppService.mainApp.status == .enabled ? .on : .off

 } catch {

 print("Login item error:", error)

 sender.state = SMAppService.mainApp.status == .enabled ? .on : .off

 }

 }

 @objc private func frontAppChanged() {

 setupAXObserver()

 applyCaptureState()

 applyAgainNextMainLoop()

 applyAfterFullscreenDebounce()

 }

 func axEvent() {

 attachAXWindows()

 applyCaptureState()

 applyAgainNextMainLoop()

 applyAfterFullscreenDebounce()

 }

 @objc private func wake() {

 setupAXObserver()

 applyCaptureState(restart: true)

 applyAgainNextMainLoop()

 applyAfterWakeDebounce()

 }

 @objc private func exit() {

 Task {

 await capture.stop()

 await MainActor.run { NSApp.terminate(nil) }

 }

 }

}

let app = NSApplication.shared

let delegate = AppDelegate()

app.delegate = delegate

_ = app.setActivationPolicy(.accessory)

app.run()

SWIFT

chmod +x 
"
${APP}
.app/Contents/MacOS/
${APP}
"

PlistBuddy 
"
${APP}
.app/Contents/Info.plist
"
 -c 
"
add CFBundleDisplayName string 
${DISPLAY_NAME}
"

PlistBuddy 
"
${APP}
.app/Contents/version.plist
"
 -c 
"
add ProjectName string 
${DISPLAY_NAME}
"

find 
"
${APP}
.app
"

open -R 
"
${APP}
.app
"

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment