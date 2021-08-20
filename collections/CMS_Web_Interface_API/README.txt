This Swagger documentation describes an API for reporting data to the CMS Quality Payment Program.

The CMS Web Interface is a user-friendly, secure, internet-based data submission mechanism for Accountable Care Organizations (ACOs) and groups of 25 or more clinicians to report quality data to the Quality Payment Program. CMS generates a sample of patients for each of the quality measures that are pre-populated in the CMS Web Interface. To assess which patients to include in each sample, CMS reviews the Medicare claims submitted by your organization during the performance period and creates a sample of patients for each measure based on the measure criteria. Your group is then asked to report on that sample of patients.

There are 10 quality measures required in the CMS Web Interface.

For each measure, you’ll be asked to provide the required data for at least the first 248 consecutive patients ranked in that measure, or all patients in the sample if you have fewer than 248 ranked in the measure.

If you are participating in the Merit-based Incentive Payment System (MIPS), your CMS Web Interface reporting will contribute to your Quality performance category score, which in turn will count toward your final MIPS score. Groups and Advanced Alternative Payment Model (APM) Entities that do not complete the minimum reporting requirement for at least one measure in the CMS Web Interface will receive a MIPS Quality performance category score of 0.

**What exactly does the WI API do?**
The WI API is designed to allow developers to programmatically enter WI submissions data from their EHR system. When you report data via the API, CMS will provide immediate, clear, and actionable feedback. By providing immediate feedback, the API enables customers to be confident that they reported their data successfully.

The following API allows you to:
1. Submit Patient Data
2. View & Prepare Samples
3. Confirm or Skip Patients
4. Track Performance
5. View Measures Specifications

**How do I authenticate?**
In order to use the API you will need to authorize using the QPP Auth Service authorization process [described here](https://qpp.cms.gov/api/auth/docs) and the resulting [JSON Web Token (JWT)](https://jwt.io/)

For more information see our [Developer Documentation](https://cmsgov.github.io/beneficiary-reporting-api-docs/)

**NOTE:** Header search parameters that contain Personally identifiable information (PII) must be base64 encoded. All headers with this requirement are identified as such on the route. The 2.0 version of Swagger does *not* encode these values for you so you will need to use code or an [online converter](https://codebeautify.org/base64-encode) to base64 encode the values to use in the Swagger UI.