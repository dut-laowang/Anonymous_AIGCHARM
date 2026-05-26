# Google Form Access Request Setup

Use a Google Form rather than a public Google Sheet. The form writes requests to a private Sheet, and the Sheet sends an email notification to the author mailbox.

## Suggested Form Fields

- Name
- Affiliation
- Email
- Intended use
- Requested materials
- Agreement to research-only use and redistribution restrictions

## Apps Script

Open the response Sheet, then use `Extensions -> Apps Script` and paste:

```javascript
function onFormSubmit(e) {
  var responses = e.namedValues;
  var subject = "[AIGenHarm-Video] New dataset access request";
  var body = "";

  for (var key in responses) {
    body += key + ": " + responses[key].join(", ") + "\n";
  }

  MailApp.sendEmail("AUTHOR_EMAIL_HERE", subject, body);
}
```

Then add a trigger:

`Triggers -> Add Trigger -> onFormSubmit -> From spreadsheet -> On form submit`.

After the public Google Form link is available, replace the website button target in `data.html`.
