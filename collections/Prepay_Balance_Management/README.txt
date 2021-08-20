## TMF API Reference: TMF654 - Prepay Balance Management

### Final : 19.5 - June 2020

The Prepay Balance Management API enables consumers to manage the balance, recharge (top-up), transfer, reserve, unreserve, deduct and balance adjustments of a  bucket. A bucket is understood in the context of this API to be an entity that keeps track of the balance available to use services. Every bucket will measure balance in different units, it can be monetary or non-monetary (e.g.: number of sms that are available, number of GB of data available, …)

### Resources
- Bucket
- TopupBalance
- AdjustBalance
- TransferBalance
- ReserveBalance
- AccumulatedBalance
- BalanceAction

### Operations
- Retrieve the balance information on a bucket for a given product (individual or aggregated).
- Retrieve the list of balance-related operations performed over a given product
- Retrieve information about all the top-up operations stored in the server filtered by some criteria.
- Perform a new top up operation (recharge)
- Retrieve detailed information about a top-up operation previously processed by the server.
- Retrieve the current and historic status information about a top-up operation previously processed by the server.
- Perform a new transfer operation
- Retrieve information about all the transfer operations stored in the server filtered by some criteria
- Retrieve detailed information about a transfer operation previously processed by the server
- Retrieve the current and historic status information about a transfer operation previously processed by the server.
- Retrieve information about all the adjustments stored in the server filtered by some criteria.
- Perform a new adjustment operation
- Retrieve detailed information about a balance adjustment operation previously processed by the server
- Reserve a balance on a bucket.
- Unreserve a balance on a bucket.
- Retrieve aggregated (accumulative) balances for a bucket.