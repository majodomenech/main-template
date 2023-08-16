# MediaTypeWithFieldIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **AllOfMediaTypeWithFieldIdentifierType** |  | 
**output_media_type** | **str** | Use the mediaType to request custom datasets in [CSV](https://www.ietf.org/rfc/rfc4180.txt) or [JSON](https://www.ietf.org/rfc/rfc8259.txt) format. CSV output from DL REST API is normalised to [XSD 1.1 types](https://www.w3.org/TR/xmlschema11-2/) such as xsd:boolean and xsd:date to facilitate ingestion. | 
**field_identifier_type** | **str** | Only valid if &#x60;outputMediaType&#x60; is set to &#x60;\&quot;text/csv\&quot;&#x60;. The identifier used for fields used in the returned CSV file. The default type depends on your account permissions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

