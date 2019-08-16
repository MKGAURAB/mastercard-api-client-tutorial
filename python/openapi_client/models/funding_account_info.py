# coding: utf-8

"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java)   # noqa: E501

    The version of the OpenAPI document: 1.2.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FundingAccountInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pan_unique_reference': 'str',
        'token_unique_reference': 'str',
        'push_account_receipt': 'str',
        'encrypted_payload': 'FundingAccountInfoEncryptedPayload'
    }

    attribute_map = {
        'pan_unique_reference': 'panUniqueReference',
        'token_unique_reference': 'tokenUniqueReference',
        'push_account_receipt': 'pushAccountReceipt',
        'encrypted_payload': 'encryptedPayload'
    }

    def __init__(self, pan_unique_reference=None, token_unique_reference=None, push_account_receipt=None, encrypted_payload=None):  # noqa: E501
        """FundingAccountInfo - a model defined in OpenAPI"""  # noqa: E501

        self._pan_unique_reference = None
        self._token_unique_reference = None
        self._push_account_receipt = None
        self._encrypted_payload = None
        self.discriminator = None

        if pan_unique_reference is not None:
            self.pan_unique_reference = pan_unique_reference
        if token_unique_reference is not None:
            self.token_unique_reference = token_unique_reference
        if push_account_receipt is not None:
            self.push_account_receipt = push_account_receipt
        if encrypted_payload is not None:
            self.encrypted_payload = encrypted_payload

    @property
    def pan_unique_reference(self):
        """Gets the pan_unique_reference of this FundingAccountInfo.  # noqa: E501

         __(CONDITIONAL)__ <br>  For repeat digitizations, the unique reference allocated to the Primary Account Number. When supplied, the tokenUniqueReferenceForPanInfo, accountNumber, expiryMonth and expiryYear must be omitted from CardInfoData. Only allowed if Only allowed if tokenUniqueReference and pushAccountReceipt are not present and encrypted data does not contain the account information. <br> __Max Length:64__   # noqa: E501

        :return: The pan_unique_reference of this FundingAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._pan_unique_reference

    @pan_unique_reference.setter
    def pan_unique_reference(self, pan_unique_reference):
        """Sets the pan_unique_reference of this FundingAccountInfo.

         __(CONDITIONAL)__ <br>  For repeat digitizations, the unique reference allocated to the Primary Account Number. When supplied, the tokenUniqueReferenceForPanInfo, accountNumber, expiryMonth and expiryYear must be omitted from CardInfoData. Only allowed if Only allowed if tokenUniqueReference and pushAccountReceipt are not present and encrypted data does not contain the account information. <br> __Max Length:64__   # noqa: E501

        :param pan_unique_reference: The pan_unique_reference of this FundingAccountInfo.  # noqa: E501
        :type: str
        """

        self._pan_unique_reference = pan_unique_reference

    @property
    def token_unique_reference(self):
        """Gets the token_unique_reference of this FundingAccountInfo.  # noqa: E501

         __(CONDITIONAL)__<br>  A unique reference assigned following the allocation of a token used to identify the token for the duration of its lifetime.  For repeat digitizations, the unique reference allocated to the token will be used to retrieve the financial account information. When supplied, the account information is omitted from FundingAccountData. Only allowed if panUniqueReference and pushAccountReceipt are not present and encrypted data does not contain the account information. <br> __Max Length:64__   # noqa: E501

        :return: The token_unique_reference of this FundingAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._token_unique_reference

    @token_unique_reference.setter
    def token_unique_reference(self, token_unique_reference):
        """Sets the token_unique_reference of this FundingAccountInfo.

         __(CONDITIONAL)__<br>  A unique reference assigned following the allocation of a token used to identify the token for the duration of its lifetime.  For repeat digitizations, the unique reference allocated to the token will be used to retrieve the financial account information. When supplied, the account information is omitted from FundingAccountData. Only allowed if panUniqueReference and pushAccountReceipt are not present and encrypted data does not contain the account information. <br> __Max Length:64__   # noqa: E501

        :param token_unique_reference: The token_unique_reference of this FundingAccountInfo.  # noqa: E501
        :type: str
        """

        self._token_unique_reference = token_unique_reference

    @property
    def push_account_receipt(self):
        """Gets the push_account_receipt of this FundingAccountInfo.  # noqa: E501

        __(CONDITIONAL)__<br> The push account receipt is supplied by the Issuer to the Merchant during a push provisioning operation. The pushAccountReceipt is then submitted by the merchant in the tokenize request and will be used by MDES to retrieve the associated funding account information. Only allowed if panUniqueReference and tokenUniqueReference are not present and encrypted data does not contain the funding account information. Refer to the <a href=\"https://developer.mastercard.com/page/push-provisioning-merchant\">Push Provisioning Use Case Guide </a>  for more information about pushAccountReceipt.  __Max Length:64__   # noqa: E501

        :return: The push_account_receipt of this FundingAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._push_account_receipt

    @push_account_receipt.setter
    def push_account_receipt(self, push_account_receipt):
        """Sets the push_account_receipt of this FundingAccountInfo.

        __(CONDITIONAL)__<br> The push account receipt is supplied by the Issuer to the Merchant during a push provisioning operation. The pushAccountReceipt is then submitted by the merchant in the tokenize request and will be used by MDES to retrieve the associated funding account information. Only allowed if panUniqueReference and tokenUniqueReference are not present and encrypted data does not contain the funding account information. Refer to the <a href=\"https://developer.mastercard.com/page/push-provisioning-merchant\">Push Provisioning Use Case Guide </a>  for more information about pushAccountReceipt.  __Max Length:64__   # noqa: E501

        :param push_account_receipt: The push_account_receipt of this FundingAccountInfo.  # noqa: E501
        :type: str
        """

        self._push_account_receipt = push_account_receipt

    @property
    def encrypted_payload(self):
        """Gets the encrypted_payload of this FundingAccountInfo.  # noqa: E501


        :return: The encrypted_payload of this FundingAccountInfo.  # noqa: E501
        :rtype: FundingAccountInfoEncryptedPayload
        """
        return self._encrypted_payload

    @encrypted_payload.setter
    def encrypted_payload(self, encrypted_payload):
        """Sets the encrypted_payload of this FundingAccountInfo.


        :param encrypted_payload: The encrypted_payload of this FundingAccountInfo.  # noqa: E501
        :type: FundingAccountInfoEncryptedPayload
        """

        self._encrypted_payload = encrypted_payload

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FundingAccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
