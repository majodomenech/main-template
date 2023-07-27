# BasePricingSourceOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Type**](Type.md) |  | 
**prefer** | [**PricingSourceDetail**](PricingSourceDetail.md) |  | [optional] 
**exclusive** | **bool** | This option applies to Bonds, and allows an exclusive pricing source to be designated when setting the pricing source for the request. If the exclusive source is not available, all fields in the Pricing and Derived Data field categories will return &#x60;N.A.&#x60; for that security. Return code &#x60;989&#x60; will be returned if the client is not privileged to see the pricing source requested. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

