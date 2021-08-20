To submit data through QPP submissions as a user, the user account must be associated with the proper organization they are trying to submit data for.  To obtain test user accounts that are associated with organizations, you will need to reserve a synthetic dataset.  A synthetic dataset will include predefined organizations, clinicians, and virtual groups with associated test user accounts.

# Reserving
1. Invoke the `/scenarios` endpoint.  You'll get a list of available scenarios.
1. Invoke the `/reserve` endpoint.  Provide the type of scenario you want to reserve and the password that will be used for the test users.  See the below Password Requirements section.

# Using a Dataset
- You now have a dataset checked out.  It may contain some combination of synthetic organizations, clinicians, virtual groups, and test user accounts.  The output from the `/reserve` endpoint outlines all the data.  You can utilize the test user accounts to login to QPP.  You can also use the other synthetic data in Submissions or the Web Interface Benificiary Sample Reporting, etc.
- Sometimes a dataset may have lingering submissions.  View the [Submissions API Documentation](https://preview.qpp.cms.gov/api/submissions/public/docs/) to learn how to delete those submissions.
- Invoking the `/list` endpoint will return all of your reserved datasets.
- To reset the password for a specific test user account in a dataset, invoke the `/resetPassword` endpoint.  See the below Password Requirements section.
- To toggle the MFA requirement on a test user account in a dataset, invoke the `/mfa` endpoint.  After setting `mfaRequired` to `true`, the next time you login into the preview environment with that user, you will be requested to set-up a second factor if you have not already set one up.
- To reset an entire dataset back it its defaults, invoke the `/setUserDefaults` endpoint.  This process runs in the background and may take some time.  See the below Password Requirements section.

# Discarding
- When you are done with a specific dataset, please discard it by invoking `/discard`.

# Password Requirements
Passwords must be at least 12 characters long and include at least one uppercase letter, lowercase letter, number, and special character.
