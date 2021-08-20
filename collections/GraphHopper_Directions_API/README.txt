
With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation,
route optimization, isochrone calculations and other tools in your application.

The GraphHopper Directions API consists of the following RESTful web services:

 * [Routing API](#tag/Routing-API),
 * [Route Optimization API](#tag/Route-Optimization-API),
 * [Isochrone API](#tag/Isochrone-API),
 * [Map Matching API](#tag/Map-Matching-API),
 * [Matrix API](#tag/Matrix-API),
 * [Geocoding API](#tag/Geocoding-API) and
 * [Cluster API](#tag/Cluster-API).

# Explore our APIs

Read through this documentation and search for key words on the left side. To unfold detailed information
about each object in the documentation, you click on e.g. `services` in the [Route Optimization documentation](#operation/solveVRP) as shown here:

![Nested Doc](./img/nested-doc.gif)

To play and see the Route Optimization API in action try our [route editor](https://graphhopper.com/blog/2015/07/21/graphhoppers-new-route-optimization-editor/)
which available in the [dashboard](https://graphhopper.com/dashboard/). See how the Routing and Geocoding API is integrated in 
our route planner website [GraphHopper Maps](https://graphhopper.com/maps) ([sources](https://github.com/graphhopper/graphhopper/tree/0.12/web/src/main/resources/assets)). 
And [see below](#section/Explore-our-APIs/Insomnia) for a collection of requests for [Insomnia](https://insomnia.rest/) and [Postman](https://www.getpostman.com/). The request file contains all example requests from this documentation.

## Get started

1. To use the GraphHopper Directions API you sign up [here](https://graphhopper.com/dashboard/#/register) and create an API key.
2. Read the documentation of the desired API part below.
3. Start using the GraphHopper Directions API. [Our API clients](#section/Explore-our-APIs/API-Clients) can speed up the integration.

To use the GraphHopper Directions API commercially, you can buy paid package [in the dashboard](https://graphhopper.com/dashboard/#/pricing).

## Contact Us

If you have problems or questions see the following information:

 * [FAQ](https://graphhopper.com/api/1/docs/FAQ/)
 * [Public forum](https://discuss.graphhopper.com/c/directions-api)     
 * [Contact us](https://www.graphhopper.com/contact-form/)

To get informed about the newest features and development follow us at [twitter](https://twitter.com/graphhopper/) or [our blog](https://graphhopper.com/blog/). 
Furthermore you can watch [this git repository](https://github.com/graphhopper/directions-api-doc) of this documentation, sign up at our [dashboard](https://graphhopper.com/dashboard/) to get the newsletter or sign up at [our forum](https://discuss.graphhopper.com/c/directions-api). Pick the channel you like most.

## API Client Libraries

To speed up development and make coding easier, we offer the following client libraries:

 * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)
 * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API

### Bandwidth reduction

If you create your own client, make sure it supports http/2 and gzipped responses for best speed.

If you use the Matrix or Route Optimization API and want to solve large problems, we recommend you to reduce bandwidth
by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4)
and specifying the header as follows: `Content-Encoding: gzip`.

## Insomnia

To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:

1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json).
2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `"api_key": your API key`
3. Start exploring

![Insomnia](./img/insomnia.png)

## Postman

To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:

1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json).
2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `"api_key": your API key`
3. Start exploring

![Postman](./img/postman.png)

# Map Data and Routing Profiles

Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers.
This chapter gives an overview about the options you have.

## OpenStreetMap

#### Geographical Coverage

[OpenStreetMap](https://www.openstreetmap.org) covers the entire world. If you want to convince yourself whether we can offer appropriate data for your region,
please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important
information is missing, for example, a weight restriction for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide)
is a beginner's guide that shows how to add data.

If you edited data, we usually consider your data after 1 week at latest.

#### Supported Vehicle Profiles

The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:

Name       | Description           | Restrictions              | Icon
-----------|:----------------------|:--------------------------|:---------------------------------------------------------
car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png)
small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png)
truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png)
scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png)
foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png)
hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png)
bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png)
mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png)
racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)

Please note:

 * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`
 * the free package supports only the vehicle profiles `car`, `bike` or `foot`
 * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.
 * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).
 * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.

 
## TomTom

If you need to consider traffic, you can purchase the TomTom add-on.

Please note:

 * currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).
 * this add-on uses the TomTom road network and historical traffic information only. Live traffic is not yet considered. Read more about [how this works](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).
 * additionally to our terms your end users need to accept the [TomTom Eula](https://www.graphhopper.com/tomtom-end-user-license-agreement/).
 * we do *not* use the TomTom web services. We only use their data with our software.
 * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.

 
[Contact us](https://www.graphhopper.com/contact-form/) for more details.

#### Geographical Coverage

We offer

- Europe including Russia
- North, Central and South America
- Saudi Arabia
- United Arab Emirates
- South Africa
- Australia

#### Supported Vehicle Profiles

Name       | Description           | Restrictions              | Icon
-----------|:----------------------|:--------------------------|:---------------------------------------------------------
car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png)
small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png)


Contact Support:
 Name: API Support
 Email: support@graphhopper.com