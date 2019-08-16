# coding: utf-8

# flake8: noqa
"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java)   # noqa: E501

    The version of the OpenAPI document: 1.2.9
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.account_holder_data import AccountHolderData
from openapi_client.models.account_holder_data_outbound import AccountHolderDataOutbound
from openapi_client.models.asset_response_schema import AssetResponseSchema
from openapi_client.models.authentication_methods import AuthenticationMethods
from openapi_client.models.billing_address import BillingAddress
from openapi_client.models.card_account_data_inbound import CardAccountDataInbound
from openapi_client.models.card_account_data_outbound import CardAccountDataOutbound
from openapi_client.models.decisioning_data import DecisioningData
from openapi_client.models.delete_request_schema import DeleteRequestSchema
from openapi_client.models.delete_response_schema import DeleteResponseSchema
from openapi_client.models.encrypted_payload import EncryptedPayload
from openapi_client.models.encrypted_payload_transact import EncryptedPayloadTransact
from openapi_client.models.error import Error
from openapi_client.models.errors_response import ErrorsResponse
from openapi_client.models.funding_account_data import FundingAccountData
from openapi_client.models.funding_account_info import FundingAccountInfo
from openapi_client.models.funding_account_info_encrypted_payload import FundingAccountInfoEncryptedPayload
from openapi_client.models.get_digital_assets_encrypted_data import GetDigitalAssetsEncryptedData
from openapi_client.models.get_digital_assets_request_schema import GetDigitalAssetsRequestSchema
from openapi_client.models.get_digital_assets_request_schema_encrypted_payload import GetDigitalAssetsRequestSchemaEncryptedPayload
from openapi_client.models.get_digital_assets_response_schema import GetDigitalAssetsResponseSchema
from openapi_client.models.get_task_status_request_schema import GetTaskStatusRequestSchema
from openapi_client.models.get_task_status_response_schema import GetTaskStatusResponseSchema
from openapi_client.models.get_token_request_schema import GetTokenRequestSchema
from openapi_client.models.get_token_response_schema import GetTokenResponseSchema
from openapi_client.models.media_content import MediaContent
from openapi_client.models.notify_token_encrypted_payload import NotifyTokenEncryptedPayload
from openapi_client.models.notify_token_updated_request_schema import NotifyTokenUpdatedRequestSchema
from openapi_client.models.notify_token_updated_response_schema import NotifyTokenUpdatedResponseSchema
from openapi_client.models.phone_number import PhoneNumber
from openapi_client.models.product_config import ProductConfig
from openapi_client.models.search_tokens_request_schema import SearchTokensRequestSchema
from openapi_client.models.search_tokens_response_schema import SearchTokensResponseSchema
from openapi_client.models.suspend_request_schema import SuspendRequestSchema
from openapi_client.models.suspend_response_schema import SuspendResponseSchema
from openapi_client.models.token import Token
from openapi_client.models.token_detail import TokenDetail
from openapi_client.models.token_detail_data import TokenDetailData
from openapi_client.models.token_detail_data_par_only import TokenDetailDataPAROnly
from openapi_client.models.token_detail_data_tcc_only import TokenDetailDataTCCOnly
from openapi_client.models.token_detail_par_only import TokenDetailPAROnly
from openapi_client.models.token_for_lcm import TokenForLCM
from openapi_client.models.token_info import TokenInfo
from openapi_client.models.tokenize_request_schema import TokenizeRequestSchema
from openapi_client.models.tokenize_response_schema import TokenizeResponseSchema
from openapi_client.models.transact_encrypted_data import TransactEncryptedData
from openapi_client.models.transact_error import TransactError
from openapi_client.models.transact_request_schema import TransactRequestSchema
from openapi_client.models.transact_response_schema import TransactResponseSchema
from openapi_client.models.un_suspend_request_schema import UnSuspendRequestSchema
from openapi_client.models.un_suspend_response_schema import UnSuspendResponseSchema
