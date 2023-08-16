# PricingSnapshotRuntimeOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **AllOfPricingSnapshotRuntimeOptionsType** |  | 
**max_embargo** | **int** | The maximum number of minutes to wait for a response containing securities subject to embargo. For example, setting &#x60;maxEmbargo&#x60; to 30 causes a response to be returned approximately 30 minutes after &#x60;snapshotTime&#x60;. The response will provide a 150 return code for any security with an embargo ([exchangeDelay](https://data.bloomberg.com/catalogs/bbg/fields/exchangeDelay/)) greater than 30 minutes, and will contain N.A. instead of prices for such securities. If &#x60;maxEmbargo&#x60; is not set, the response will be returned once embargo periods have completed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

