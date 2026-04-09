---
title: Native Secure Enclaved backed ssh keys on MacOS · GitHub
url: https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf
site_name: hackernews_api
fetched_at: '2025-11-24T11:06:50.782739'
original_url: https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf
author: arianvanp
date: '2025-11-23'
description: 'Native Secure Enclaved backed ssh keys on MacOS . GitHub Gist: instantly share code, notes, and snippets.'
tags:
- hackernews
- trending
---

Instantly share code, notes, and snippets.

# arianvp/SSH_MACOS_SECURE_ENCLAVES.md

 Last active

November 24, 2025 10:53



Show Gist options



* Download ZIP





* Star227(227)You must be signed in to star a gist
* Fork25(25)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf to your computer and use it in GitHub Desktop.



Embed

# Select an option



* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found





Learn more about clone URLs





 Clone this repository at &lt;script src=&quot;https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf.js&quot;&gt;&lt;/script&gt;





Save arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf to your computer and use it in GitHub Desktop.

Download ZIP

 Native Secure Enclaved backed ssh keys on MacOS




Raw

 SSH_MACOS_SECURE_ENCLAVES.md


# Native Secure Enclave backed ssh keys on MacOS

It turns out that MacOS Tahoe can generate and use secure-enclave backed SSH keys! This replaces projects likehttps://github.com/maxgoedjen/secretive

There is a shared library/usr/lib/ssh-keychain.dylibthat traditionally has been used to add smartcard support
to ssh by implementingPKCS11Providerinterface. However since recently it also implementsSecurityKeyProivderwhich supports loading keys directly from the secure enclave!SecurityKeyProvideris what is normally used to talk to FIDO2 devices (e.g.libfido2can be used to talk to your Yubikey). However you can now use it to talk to your Secure Enclave instead!

recording.mov

## Key setup

Seeman sc_authandman ssh-keychainfor all the options

To create a Secure Enclave backed key that requires biometrics, run the
following command and press TouchID:

% sc_auth create-ctk-identity -l ssh -k p-256-ne -t bio

You can confirm that the key was create with thelist-ctk-identitiescommand:

arian@Mac ssh-keychain % sc_auth list-ctk-identities
Key Type Public Key Hash Prot Label Common Name Email Address Valid To Valid
p-256-ne A71277F0BC5825A7B3576D014F31282A866EF3BC bio ssh ssh 23.11.26, 17:09 YES

It also supports listing the ssh key fingerprints instead:

% sc_auth list-ctk-identities -t ssh
Key Type Public Key Hash Prot Label Common Name Email Address Valid To Valid
p-256-ne SHA256:vs4ByYo+T9M3V8iiDYONMSvx2k5Fj2ujVBWt1j6yzis bio ssh ssh 23.11.26, 17:09 YES

Keys can be deleted with

% sc_auth delete-ctk-identity -h <Public Key Hash>

## Usage withssh

You can "download" the public / private keypair from the secure enclave using the following command:

% ssh-keygen -w /usr/lib/ssh-keychain.dylib -K -N ""
Enter PIN for authenticator:
You may need to touch your authenticator to authorize key download.
Saved ECDSA-SK key to id_ecdsa_sk_rk
% cat id_ecdsa_sk_rk.pub
sk-ecdsa-sha2-nistp256@openssh.com AAAAInNrLWVjZHNhLXNoYTItbmlzdHAyNTZAb3BlbnNzaC5jb20AAAAIbmlzdHAyNTYAAABBBKiHAiAZhcsZ95n85dkNGs9GnbDt0aNOia2gnuknYV2wKL3y0u+d3QrE9cFkmWXIymHZMglL+uJA+6mShY8SeykAAAAEc3NoOg== ssh:

You can just use the empty string for PIN. For some reasonopensshalways asks for
it even if the authenticator in question does not use a PIN but a biometric.
Note that the "private" key here is just a reference to the FIDO credential. It does
not contain any secret key material. Hence I'm specifiyng-N ""to skip an encryption
passphrase.

Now if you copy this public key to your authorized keys file, it should work!

% ssh-copy-id -i id_ecdsa_sk_rk localhost
% ssh -o SecurityKeyProvider=/usr/lib/ssh-keychain.dylib localhost

## Usage withssh-agent

Instead of downloading the public/private keypair to a file you can also directly
make the keys available tossh-agent. For this you can use the following command:

% ssh-add -K -S /usr/lib/ssh-keychain.dylib
Enter PIN for authenticator:
Resident identity added: ECDSA-SK SHA256:vs4ByYo+T9M3V8iiDYONMSvx2k5Fj2ujVBWt1j6yzis
% ssh-add -L
sk-ecdsa-sha2-nistp256@openssh.com AAAAInNrLWVjZHNhLXNoYTItbmlzdHAyNTZAb3BlbnNzaC5jb20AAAAIbmlzdHAyNTYAAABBBKiHAiAZhcsZ95n85dkNGs9GnbDt0aNOia2gnuknYV2wKL3y0u+d3QrE9cFkmWXIymHZMglL+uJA+6mShY8SeykAAAAEc3NoOg==
% ssh-copy-id localhost
% ssh -o SecurityKeyProvider=/usr/lib/ssh-keychain.dylib localhost

## Using the SecurityKeyProvider by default

SecurityKeyProvidercan be configured in.ssh/configbut I recommend settingexport SSH_SK_PROVIDER=/usr/lib/ssh-keychain.dylibin your.zprofileinstead as
that environment variable gets picked up byssh,ssh-addandssh-keygen.

This means you can just do:

ssh-add -K
ssh my-server

or

ssh-keygen -K
ssh -i id_ecdsa_rk_sk my-server

to ssh into your server

## Exportable keys

There's also an exportable variant where the private key is encrypted using the secure enclave as opposed to generated on the secure enclave. This is might be considered less secure but is convenient for key backup.

% sc_auth create-ctk-identity -l ssh-exportable -k p-256 -t bio
% sc_auth list-ctk-identities
p-256 A581E5404ED157C4C73FFDBDFC1339E0D873FCAE bio ssh-exportable ssh-exportable 23.11.26, 19:50 YES
% sc_auth export-ctk-identity -h A581E5404ED157C4C73FFDBDFC1339E0D873FCAE -f ssh-exportable.pem
Enter a password which will be used to protect the exported items:
Verify password:

You can then re-import it on another device

% sc_auth import-ctk-identities -f ssh-exportable.pem.p12 -t bio
Enter PKCS12 file password:



### sandstromcommentedNov 23, 2025

Is it possible to use the.biometryCurrentSetflag with this approach?

https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/biometrycurrentset

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### arianvpcommentedNov 23, 2025

No unfortunately not. It's biometrics on or off. No other controls.

I wonder if you create such a key with Security framework yourself if they can get picked up by ssh-keychain.dylib though? That might be a way.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### arianvpcommentedNov 23, 2025

@sandstromI reverse-engineered thessh-keychain.dylibusing binary ninja and some help of Claude.

I'm pretty sure I can add ansk_enroll()to this that does thebiometryCurrentSetstuff

#
import

<
Foundation/Foundation.h
>

#
import

<
Security/Security.h
>

#
include

<
string.h
>

#
include

<
CommonCrypto/CommonDigest.h
>

#
include

"
../openssh-portable/sk-api.h
"

//
 Global signature counter

static

uint32_t
 signatureCounter =
0
;

//
 Helper category for NSMutableData

@interface

NSMutableData
 (Helpers)
- (
void
)
appendUInt8
:
(
uint8_t
)
value
;
- (
void
)
appendUInt32
:
(
uint32_t
)
value
;

@end

@implementation

NSMutableData
 (Helpers)
- (
void
)
appendUInt8
:
(
uint8_t
)
value
 {
 [
self

appendBytes:
&value
length:
sizeof
(value)];
}

- (
void
)
appendUInt32
:
(
uint32_t
)
value
 {

//
 Big endian (network byte order)


uint8_t
 bytes[
4
] = {
 (value >>
24
) &
0xFF
,
 (value >>
16
) &
0xFF
,
 (value >>
8
) &
0xFF
,
 value &
0xFF

 };
 [
self

appendBytes:
bytes
length:
sizeof
(bytes)];
}

@end

int32_t

sk_load_resident_keys
(
const

char
 *pin,

struct
 sk_option **options,

struct
 sk_resident_key ***rks,

size_t
 *nrks) {

//
 Build the keychain query


NSDictionary
 *query = @{
 (__bridge
id
)
kSecClass
: (__bridge
id
)
kSecClassKey
,
 (__bridge
id
)
kSecAttrKeyClass
: (__bridge
id
)
kSecAttrKeyClassPrivate
,
 (__bridge
id
)
kSecAttrKeyType
: (__bridge
id
)
kSecAttrKeyTypeECSECPrimeRandom
,
 (__bridge
id
)
kSecAttrAccessGroup
: (__bridge
id
)
kSecAttrAccessGroupToken
,
 (__bridge
id
)
kSecAttrKeySizeInBits
: @
256
,
 (__bridge
id
)
kSecReturnRef
: @
YES
,
 (__bridge
id
)
kSecReturnAttributes
: @
YES
,
 (__bridge
id
)
kSecMatchLimit
: (__bridge
id
)
kSecMatchLimitAll

 };


//
 Query the keychain

 CFTypeRef result =
NULL
;
 OSStatus status =
SecItemCopyMatching
((__bridge CFDictionaryRef)query, &result);


if
 (status != errSecSuccess) {

NSLog
(
@"
Failed to load resident keys:
%d
"
, (
int
)status);

return
 -
1
;
 }


NSArray
 *keys = (__bridge_transfer
NSArray
 *)result;


//
 Allocate result array

 *nrks = keys.
count
;
 *rks =
calloc
(keys.
count
,
sizeof
(
struct
 sk_resident_key *));


//
 Process each key


NSUInteger
 rkIndex =
0
;

for
 (
NSDictionary
 *keyDict in keys) {

//
 Get the key reference and extract its attributes

 SecKeyRef privateKey = (__bridge SecKeyRef)keyDict[(__bridge
id
)
kSecValueRef
];
 SecKeyRef publicKey =
SecKeyCopyPublicKey
(privateKey);


if
 (!publicKey) {

continue
;
 }


NSDictionary
 *attributes = (__bridge_transfer
NSDictionary
 *)
SecKeyCopyAttributes
(publicKey);


//
 Extract the public key data and application label


NSData
 *publicKeyData = attributes[(__bridge
id
)
kSecValueData
];

NSData
 *applicationLabel = attributes[(__bridge
id
)
kSecAttrApplicationLabel
];


if
 (!publicKeyData || !applicationLabel) {

CFRelease
(publicKey);

continue
;
 }


//
 Allocate and populate the resident key structure


struct
 sk_resident_key *rk =
calloc
(
1
,
sizeof
(
struct
 sk_resident_key));

 rk->
alg
 =
0
;
//
 Algorithm would be determined from key attributes

 rk->
slot
 =
0
;
 rk->
application
 =
strdup
(
"
ssh:
"
);
 rk->
flags
 =
1
;


//
 Allocate and copy public key

 rk->
key
.
flags
 =
1
;
 rk->
key
.
public_key_len
 = publicKeyData.
length
;
 rk->
key
.
public_key
 =
malloc
(publicKeyData.
length
);

memcpy
(rk->
key
.
public_key
, publicKeyData.
bytes
, publicKeyData.
length
);


//
 Allocate and copy key handle

 rk->
key
.
key_handle_len
 = applicationLabel.
length
;
 rk->
key
.
key_handle
 =
malloc
(applicationLabel.
length
);

memcpy
(rk->
key
.
key_handle
, applicationLabel.
bytes
, applicationLabel.
length
);

 (*rks)[rkIndex++] = rk;


CFRelease
(publicKey);
 }


return

0
;
}

uint32_t

sk_api_version
(
void
) {

return
 SSH_SK_VERSION_MAJOR;
}

int

sk_enroll
(
uint32_t
 alg,
const

uint8_t
 *challenge,
size_t
 challenge_len,

const

char
 *application,
uint8_t
 flags,
const

char
 *pin,

struct
 sk_option **options,
struct
 sk_enroll_response **enroll_response) {

//
 Not implemented


return
 SSH_SK_ERR_UNSUPPORTED;
}

int

sk_sign
(
uint32_t
 alg,
const

uint8_t
 *data,
size_t
 data_len,

const

char
 *application,
const

uint8_t
 *key_handle,
size_t
 key_handle_len,

uint8_t
 flags,
const

char
 *pin,
struct
 sk_option **options,

struct
 sk_sign_response **sign_response) {


//
 Only support ECDSA for now


if
 (alg != SSH_SK_ECDSA) {

return
 SSH_SK_ERR_UNSUPPORTED;
 }


//
 Create NSData from key_handle


NSData
 *keyHandle = [
NSData

dataWithBytes:
key_handle
length:
key_handle_len];


//
 Build query to find the private key


NSDictionary
 *query = @{
 (__bridge
id
)
kSecClass
: (__bridge
id
)
kSecClassKey
,
 (__bridge
id
)
kSecAttrApplicationLabel
: keyHandle,
 (__bridge
id
)
kSecAttrKeyType
: (__bridge
id
)
kSecAttrKeyTypeECSECPrimeRandom
,
 (__bridge
id
)
kSecAttrAccessGroup
: (__bridge
id
)
kSecAttrAccessGroupToken
,
 (__bridge
id
)
kSecReturnRef
: @
YES

 };


//
 Query the keychain for the private key

 CFTypeRef secKey =
NULL
;
 OSStatus status =
SecItemCopyMatching
((__bridge CFDictionaryRef)query, &secKey);


if
 (status != errSecSuccess) {

NSLog
(
@"
Failed to find key for signing:
%d
"
, (
int
)status);

return
 SSH_SK_ERR_DEVICE_NOT_FOUND;
 }


//
 Hash the application string (SHA-256)


NSMutableData
 *applicationHash = [
NSMutableData

dataWithLength:
CC_SHA256_DIGEST_LENGTH];

CC_SHA256
(application, (CC_LONG)
strlen
(application), applicationHash.
mutableBytes
);


//
 Hash the data to be signed (SHA-256)


NSMutableData
 *dataHash = [
NSMutableData

dataWithLength:
CC_SHA256_DIGEST_LENGTH];

CC_SHA256
(data, (CC_LONG)data_len, dataHash.
mutableBytes
);


//
 Build authenticator data according to FIDO spec


//
 authenticatorData = rpIdHash (32) + flags (1) + counter (4) + dataHash (32)


NSMutableData
 *authData = [
NSMutableData

dataWithCapacity:
applicationHash.length + dataHash.length +
5
];
 [authData
appendData:
applicationHash];
 [authData
appendUInt8:
flags];


//
 Increment and append signature counter

 signatureCounter++;
 [authData
appendUInt32:
signatureCounter];
 [authData
appendData:
dataHash];


//
 Hash the authenticator data


NSMutableData
 *authDataHash = [
NSMutableData

dataWithLength:
CC_SHA256_DIGEST_LENGTH];

CC_SHA256
(authData.
bytes
, (CC_LONG)authData.
length
, authDataHash.
mutableBytes
);


//
 Sign the hash

 CFErrorRef error =
NULL
;
 CFDataRef signature =
SecKeyCreateSignature
((SecKeyRef)secKey,

kSecKeyAlgorithmECDSASignatureRFC4754
,
 (__bridge CFDataRef)authDataHash,
 &error);


if
 (!signature) {

NSLog
(
@"
Failed to create signature:
%@
"
, error);

if
 (error)
CFRelease
(error);

CFRelease
(secKey);

return
 SSH_SK_ERR_GENERAL;
 }


//
 Allocate response structure


struct
 sk_sign_response *resp =
calloc
(
1
,
sizeof
(
struct
 sk_sign_response));


//
 The signature is 64 bytes for P-256: 32 bytes r + 32 bytes s


NSData
 *sigData = (__bridge_transfer
NSData
 *)signature;

size_t
 halfLen = sigData.
length
 /
2
;

 resp->
sig_r_len
 = halfLen;
 resp->
sig_r
 =
malloc
(halfLen);

memcpy
(resp->
sig_r
, sigData.
bytes
, halfLen);

 resp->
sig_s_len
 = halfLen;
 resp->
sig_s
 =
malloc
(halfLen);

memcpy
(resp->
sig_s
, sigData.
bytes
 + halfLen, halfLen);

 resp->
flags
 = flags;
 resp->
counter
 = signatureCounter;

 *sign_response = resp;


CFRelease
(secKey);


return

0
;
}

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### arianvpcommentedNov 23, 2025

Something like this probably works:

But I think I need an Apple Developer Programme account, as I need to codesign the dylib to be able to access the secure enclave

int

sk_enroll
(
uint32_t
 alg,
const

uint8_t
 *challenge,
size_t
 challenge_len,

const

char
 *application,
uint8_t
 flags,
const

char
 *pin,

struct
 sk_option **options,
struct
 sk_enroll_response **enroll_response) {


//
 Create access control with biometry requirement

 CFErrorRef error =
NULL
;
 SecAccessControlRef access =
SecAccessControlCreateWithFlags
(

kCFAllocatorDefault
,

kSecAttrAccessibleWhenUnlockedThisDeviceOnly
,

kSecAccessControlPrivateKeyUsage
 |
kSecAccessControlBiometryCurrentSet
,
 &error
 );


if
 (!access) {

NSLog
(
@"
Failed to create access control:
%@
"
, error);

if
 (error)
CFRelease
(error);

return
 SSH_SK_ERR_GENERAL;
 }


//
 Create key attributes for Secure Enclave P-256 key


NSDictionary
 *keyAttrs = @{
 (__bridge
id
)
kSecAttrKeyType
: (__bridge
id
)
kSecAttrKeyTypeECSECPrimeRandom
,
 (__bridge
id
)
kSecAttrKeySizeInBits
: @
256
,
 (__bridge
id
)
kSecAttrTokenID
: (__bridge
id
)
kSecAttrTokenIDSecureEnclave
,
 (__bridge
id
)
kSecPrivateKeyAttrs
: @{
 (__bridge
id
)
kSecAttrIsPermanent
: @
YES
,
 (__bridge
id
)
kSecAttrAccessControl
: (__bridge_transfer
id
)access,
 (__bridge
id
)
kSecAttrApplicationLabel
: [
NSString

stringWithUTF8String:
application],
 }
 };


//
 Generate the key pair

 SecKeyRef privateKey =
SecKeyCreateRandomKey
((__bridge CFDictionaryRef)keyAttrs, &error);


if
 (!privateKey) {

NSLog
(
@"
Failed to create key:
%@
"
, error);

if
 (error)
CFRelease
(error);

return
 SSH_SK_ERR_GENERAL;
 }


//
 Get the public key

 SecKeyRef publicKey =
SecKeyCopyPublicKey
(privateKey);

if
 (!publicKey) {

CFRelease
(privateKey);

return
 SSH_SK_ERR_GENERAL;
 }


//
 Get public key data

 CFErrorRef exportError =
NULL
;
 CFDataRef publicKeyData =
SecKeyCopyExternalRepresentation
(publicKey, &exportError);

if
 (!publicKeyData) {

NSLog
(
@"
Failed to export public key:
%@
"
, exportError);

if
 (exportError)
CFRelease
(exportError);

CFRelease
(publicKey);

CFRelease
(privateKey);

return
 SSH_SK_ERR_GENERAL;
 }


//
 Get the application label (this serves as the key handle)


NSDictionary
 *publicKeyAttrs = (__bridge_transfer
NSDictionary
 *)
SecKeyCopyAttributes
(publicKey);

NSData
 *applicationLabel = publicKeyAttrs[(__bridge
id
)
kSecAttrApplicationLabel
];


if
 (!applicationLabel) {

CFRelease
(publicKeyData);

CFRelease
(publicKey);

CFRelease
(privateKey);

return
 SSH_SK_ERR_GENERAL;
 }


//
 Allocate response structure


struct
 sk_enroll_response *resp =
calloc
(
1
,
sizeof
(
struct
 sk_enroll_response));


//
 Copy public key


NSData
 *pubKeyNSData = (__bridge
NSData
 *)publicKeyData;
 resp->
public_key_len
 = pubKeyNSData.
length
;
 resp->
public_key
 =
malloc
(resp->
public_key_len
);

memcpy
(resp->
public_key
, pubKeyNSData.
bytes
, resp->
public_key_len
);


//
 Copy key handle (application label)

 resp->
key_handle_len
 = applicationLabel.
length
;
 resp->
key_handle
 =
malloc
(resp->
key_handle_len
);

memcpy
(resp->
key_handle
, applicationLabel.
bytes
, resp->
key_handle_len
);


//
 Set flags

 resp->
flags
 = flags;


//
 Note: We're not implementing attestation for now


//
 resp->attestation_cert and resp->signature would be set here

 resp->
attestation_cert
 =
NULL
;
 resp->
attestation_cert_len
 =
0
;
 resp->
signature
 =
NULL
;
 resp->
signature_len
 =
0
;

 *enroll_response = resp;


CFRelease
(publicKeyData);

CFRelease
(publicKey);

CFRelease
(privateKey);


return

0
;
}

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### sandstromcommentedNov 24, 2025

I reverse-engineered the ssh-keychain.dylib using binary ninja and some help of Claude.

Wow! 🙂

Asking because setting.biometryCurrentSetis a nice feature in Secretive, since it (a) makes it impossible to extract the key and (b) if we know who setup the biometrics, it's impossible to later add new biometrics [without discarding keys] to circumvent.

Nice to hear that it might be possible with this approach too!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.





Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
