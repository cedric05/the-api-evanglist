**TMF API Reference : TMF - 644 Privacy**

**Release : 19.0 - June 2019**

The Privacy Management API provides standardized mechanism for privacy profile specification, privacy profiles and privacy agreements such as creation, update, retrieval, deletion and notification of events.Privacy management API manages the following data resources:

**Privacy Profile specification**
Privacy profile specification represents a description for privacy profiles.Main privacy profile specification attributes are its identifier, name, description, version, last update, lifecycle status, validity period, characteristics and their values, related parties, applicable roles.

**Privacy Profile**
Privacy profile represents the set of Privacy settings defined for a Party.Main privacy profile attributes are its identifier, name, description, date of creation, status, validity period, privacy profile specification, characteristics values, agreement, the party who has agreed and the party which the privacy is applicable for, typically the same party represents both the aggreged by and applicable for. In case of minor privacy the applicable for party is the minor and the agreed party is the parent.

**Privacy Agreement**
Privacy agreement represents the approval made by the Party about a Party Privacy Profile.Main privacy agreement attributes are its identifier, name, description, agreement period, initial date, completion date, document number, statement of intent, status, type, version, agreement specification, agreement items, engaged party, agreement authorization, characteristics, associated agreements, privacy profile and privacy profile characteristic values.
Privacy management API performs the following operations on privacy profile specification, privacy profiles and privacy agreements:
-Retrieval of a privacy profile specification, a privacy profile or a privacy agreement, or of a collection of them depending on filter criteria
-Partial update of a privacy profile specification, a privacy profile or a privacy agreement
-Creation of a privacy profile specification, a privacy profile or a privacy agreement
-Deletion of a privacy profile specification, a privacy profile or a privacy agreement (for administration purposes)

**Notification of events:**
-privacy profile specification create
-privacy profile specification update
-privacy profile specification delete
-privacy profile create
-privacy profile update
-privacy profile delete
-privacy agreement create
-privacy agreement update


Copyright © TM Forum 2019. All Rights Reserved


