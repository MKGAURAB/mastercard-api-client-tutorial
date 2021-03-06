# AccountHolderDataOutbound

__(CONDITIONAL)__<br> Present in tokenize response if supported by the Merchant, if using a pushAccountReceipt and if there is account holder data associated with the pushAccountReceipt in case that the issuer decision is APPROVED. Refer to <a href=\"https://developer.mastercard.com/devzone/api/portal/download/0000016a-f9a1-d055-ad7a-f9efc8d50000\">MDES Token Connect Token Requestor Implementation Guide and Specification </a> for more details. </br> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder_name** | **str** | __(OPTIONAL)__ The name of the cardholder&lt;br&gt; __Max Length:27__  | [optional] 
**account_holder_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**account_holder_email_address** | **str** | __(OPTIONAL)__ The e-mail address of the Account Holder&lt;br&gt; __Max Length:320__  | [optional] 
**account_holder_mobile_phone_number** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


