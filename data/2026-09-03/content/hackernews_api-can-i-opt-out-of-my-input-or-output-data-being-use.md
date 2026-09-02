---
title: Can I opt out of my input or output data being used for training? | Mistral Help Center
url: https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training
site_name: hackernews_api
content_file: hackernews_api-can-i-opt-out-of-my-input-or-output-data-being-use
fetched_at: '2026-09-03T07:20:31.472713'
original_url: https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training
author: teekert
date: '2026-09-02'
tags:
- hackernews
- trending
---

In certain cases, your input and output data (such as conversations, documents, and other user-provided content)may be included in Mistral’s model training programs.

🔑 You retain full control over this processing and have the right toopt out of these programs at any time.

The opt-out processdepends on the service or platform used, as described below.

 

# Opt out of Vibe data training (via the Admin panel)

🔑Vibe:users arenot opted out by defaultand can opt out at any time in their settings.Vibe (Enterprise):customers areopted out of training by default— the opt-in toggle is managed at the admin level.

You canopt out of trainingthrough theAdmin panelby following the procedure below:

1. SelectVibeunder theManagesection.
2. Under thePrivacysection,disablethe toggle labelledAllow your interactions to be used to train our models.

📌 Documents attached or uploaded within Vibeare considered as input data. Therefore, you may wish to opt out to prevent such documents from being used to improve Mistral’s models.

🔑 Once the opt-out is confirmed,Mistral no longer uses your input or output datafor the purpose of training its models.

 

# Opt out of Vibe data training on the mobile application (iOS and Android)

On bothiOSandAndroid, the opt-out procedure is as follows:

1. Open theSettingspage of the application.
2. SelectData & Account Controlsunder theAccountsection.
3. In theData & Account Controlspanel,deselecttheEnable data sharingcheckbox to opt out of Mistral’s training program.
 

# Opt out of Mistral Studio and API data training (via the Admin panel)

🔑 Customers retain full control over this processing and have the right to opt out at any time.

You may opt out of data training forMistral Studioand relatedAPI servicesby following the steps below:

1. In theAdmin panel, open thePrivacymenu in the left-hand navigation bar.
2. Under theAnonymous improvement datasection,disablethe toggle to prevent API calls and related data from being used to improve Mistral’s services.

🔑Vibe and API opt-out toggles are separate.Opting out of one does not opt you out of the other — you must configure each toggle individually.

Did this answer your question?

## Related Articles

* Can I activate Zero Data Retention (ZDR)?
* Do you use my user data to train your Artificial Intelligence models?
* Can other people view my conversations?
* How can I exercise my GDPR rights?
* How do you handle my data when using the Memories feature?