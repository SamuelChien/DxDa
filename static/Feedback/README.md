# Office Browser Feedback

This is a web sdk which adds feedback capabilities to your web application or website. Adding the sdk takes minimal effort and you get a customizable user feedback form which can take screenshots of the browser window and will send the feedback to Office Customer Voice (OCV).

## Register your web app

Before using the SDK register you web app with Office Customer Voice and get a unique appId.

## Developer guide

Download the sdk and host its files as part of your website. Load the sdk as shown below, set the init options and the sdk will make available globally methods to launch the feedback experience. You can now attach these methods to any event on your website. Normally you will create a feedback button on your website and attach the feedback method to it's onclick event.

### Downloading the sdk
The sdk can be downloaded from the Office Internal Shared Source (OfficeISS) feed.
* [NuGet](https://office.visualstudio.com/CLE/In%20App%20Feedback/_apps/hub/ms.feed.feed-hub?feedName=OfficeISS&protocolType=NuGet&packageName=officebrowserfeedback).
* [Npm](https://office.visualstudio.com/CLE/In%20App%20Feedback/_apps/hub/ms.feed.feed-hub?feedName=OfficeISS&protocolType=Npm&packageName=officebrowserfeedback)

### Loading the sdk

Load the sdk using the following code given in index.html.
```javascript
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) { return; }
    js = d.createElement(s); js.id = id;
    js.src = "scripts/OfficeBrowserFeedback.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'officebrowserfeedback-jssdk'));
```
Set the correct url for the script file in the above code. All this code does is to dynamically add a `<script>` tag to the DOM. This ensures cross browser asynchronous and deferred script loading. Note you do not need to manually load the styles or the intl file, just point the sdk to them in the init options and it will lazily load them.

### Init options

Init options are passed to the sdk by setting the `OfficeBrowserFeedback.initOptions` object. Remember to set the `OfficeBrowserFeedback` object before setting the init options.
```javascript
window.OfficeBrowserFeedback = window.OfficeBrowserFeedback || {};
```
Following are the available init options:
* appId: [number] An id uniquely identifying your app in the OCV world.
* stylesUrl: [string] The url for the styles file. The SDK loads it for you.
* intlUrl: [string] The url of the intl/ folder.
* environment: [number] 0 - Prod, 1 - Test. This determines whether the feedback will go to the production pipeline or not.
* sessionID: [string] (optional but strongly recommended) A string uniquely identifying the current session. This will appear in the feedback payload.
* build: [string] (optional but strongly recommended) A build version which will appear in the feedback payload. Must be in the form 
```
    ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,5}(\.[0-9]{1,5})?$
```
* primaryColour: [string] (optional) The primary theme colour of the ui in hex eg. #bada55 or #abc. This should be dark enough to easily read white text on it.
* secondaryColour: [string] (optional) The secondary theme colour of the ui in hex eg. #bada55 or #abc. This should be dark enough to easily read white text on it.
* onDismiss: [function] (optional) Delegate to be called when the feedback ui is dismissed. Signature is
```javascript
    // submitted: True if feedback was successfully submitted and then the ui was dismissed. False otherwise.
    (submitted: Boolean): void;
```
* locale: [string] (optional) The UI locale of the calling page, if you need localization.
* bugForm: [boolean] (optional default:false) Whether to include a bug form or not.
* userEmail: [string] (optional) The user's email if known. This will be prefilled in the feedback form if specified.
* screenshot: [boolean] (optional default:true) Whether to include screenshot functionality or not. If enabled the the user will have the option to attach a screenshot.
* userVoice: [object] (optional) If specified the user will be directed to User Voice if they have a suggestion. Should have the following properties:
```javascript
    // Url for user voice.
    url: string;
    // Url for the user voice terms of service
    termsOfServiceUrl: string;
    // Url for the user voice privacy policy
    privacyPolicyUrl: string;
```

### Using the sdk

Attach the following handlers to any event on your website.
Handlers:
* `window.OfficeBrowserFeedback.multiFeedback()`: Opens a two step dialog where the user manually chooses the kind of feedback.
* `window.OfficeBrowserFeedback.singleFeedback(string feedbackType)`: Opens a single step dialog where the feedbackType is predetermined. `feedbacktype` can be `"Smile"`,`"Frown"` or `"Bug"`.

### Other considerations

* The namespace is only polluted with `window.OfficeBrowserFeedback`.
* The stylesheet only targets classes and ids. All classes and ids used by the sdk carry the prefix **obf-**.
* Each handler returns a Promise object. Should the handler not function as expected, attach a .then() or .catch() to investigate why the Promise is being rejected. Eg.
```javascript
    OfficeBrowserFeedback.multiFeedback().then(
        function () { console.log('suceeded'); },
        function (err) { console.log('failed with error: ' + err); });
```
   
