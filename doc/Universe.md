# Universe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**Context**](Context.md) |  | 
**id** | **AllOfUniverseId** |  | 
**type** | **AllOfUniverseType** |  | 
**identifier** | [**ComponentIdentifier**](ComponentIdentifier.md) |  | 
**referenced_by_active_requests** | [**ReferencedByActiveRequests**](ReferencedByActiveRequests.md) |  | 
**contains** | [**list[UniverseItem]**](UniverseItem.md) | List of identifiers. DL REST API supports up to 80,000 securities in a universe without security overrides. If the universe contains security overrides, Bloomberg recommends limiting the universe size to 20,000 securities. | 
**title** | [**Title**](Title.md) |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**issued** | [**Issued**](Issued.md) |  | 
**modified** | [**Modified**](Modified.md) |  | 
**total_items** | [**TotalItems**](TotalItems.md) |  | 
**page_count** | [**PageCount**](PageCount.md) |  | 
**view** | [**PaginatedView**](PaginatedView.md) |  | 
**security_overrides_defined** | **bool** | True if a field override is defined in this universe. False if no field overrides are defined in this universe. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

