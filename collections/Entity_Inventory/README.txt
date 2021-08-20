## TMF API Reference : TMF 703 - Entity Inventory 

 Version 4.0 

The intent of this API is to provide a consistent/standardized mechanism to query and manipulate the Entity inventory.

The Entity Inventory API can be used to query the Entity and Association instances. 
 Note: The Entity Inventory API can be called by an order management system to create new Entity/Association instances or update existing Entity/Association instances in the Entity Inventory.

### Entity/Association resources

### Entity Inventory API performs the following operations on Entity/Association resources :
- Retrieve  an Entity/Association or a collection of Entities/Associations depending on filter criteria
- Partial update of an Entity/Association instance (including updating rules)
- Create an Entity/Association instance (including default values and creation rules)
- Delete an Entity/Association (for administration users only)
- Notification of events on Entity/Association 
 it should be noted that the Entity resource can be considered as an abstract resource that extended by a concrete Managed Entity resource in this API

Copyright (c)TM Forum 2020. All Rights Reserved.