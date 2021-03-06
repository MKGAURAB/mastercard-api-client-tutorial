/* 
 * MDES for Merchants
 *
 * The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 
 *
 * The version of the OpenAPI document: 1.2.10
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using OpenAPIDateConverter = Acme.App.MastercardApi.Client.Client.OpenAPIDateConverter;

namespace Acme.App.MastercardApi.Client.Model
{
    /// <summary>
    /// TokenInfo
    /// </summary>
    [DataContract]
    public partial class TokenInfo :  IEquatable<TokenInfo>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TokenInfo" /> class.
        /// </summary>
        /// <param name="tokenPanSuffix">The last few digits (typically four) of the Token PAN.&lt;br&gt;     __Max Length:8__&lt;br&gt; __Required: Yes__ .</param>
        /// <param name="accountPanSuffix">The last few digits (typically four) of the Account PAN.&lt;br&gt;     __Max Length:8__&lt;br&gt; __Required: Yes__ .</param>
        /// <param name="tokenExpiry">The expiry of the Token PAN, given in MMYY format.&lt;br&gt;     __Max Length:4__&lt;br&gt; __Required: Yes__ .</param>
        /// <param name="accountPanExpiry">The expiry of the Account PAN, given in MMYY format. &lt;br&gt; __Max Length: 4__&lt;br&gt; __Required: No__ .</param>
        /// <param name="dsrpCapable">Whether DSRP transactions are supported by this Token. Must be either &#39;true&#39; (DSRP capable) or &#39;false&#39; (Not DSRP capable).&lt;br&gt; __Max Length: 5__&lt;br&gt; __Required: Yes__ .</param>
        /// <param name="tokenAssuranceLevel">A value indicating the confidence level of the token to Account PAN binding.&lt;br&gt;     __Max Length:2__&lt;br&gt; __Required: No__ .</param>
        /// <param name="productCategory">The product category of the Account PAN. When supplied will be one of the following values -  * CREDIT * DEBIT * PREPAID * UNKNOWN  __Max Length: 32__&lt;br&gt; __Required: No__ .</param>
        public TokenInfo(string tokenPanSuffix = default(string), string accountPanSuffix = default(string), string tokenExpiry = default(string), string accountPanExpiry = default(string), string dsrpCapable = default(string), string tokenAssuranceLevel = default(string), string productCategory = default(string))
        {
            this.TokenPanSuffix = tokenPanSuffix;
            this.AccountPanSuffix = accountPanSuffix;
            this.TokenExpiry = tokenExpiry;
            this.AccountPanExpiry = accountPanExpiry;
            this.DsrpCapable = dsrpCapable;
            this.TokenAssuranceLevel = tokenAssuranceLevel;
            this.ProductCategory = productCategory;
        }
        
        /// <summary>
        /// The last few digits (typically four) of the Token PAN.&lt;br&gt;     __Max Length:8__&lt;br&gt; __Required: Yes__ 
        /// </summary>
        /// <value>The last few digits (typically four) of the Token PAN.&lt;br&gt;     __Max Length:8__&lt;br&gt; __Required: Yes__ </value>
        [DataMember(Name="tokenPanSuffix", EmitDefaultValue=false)]
        public string TokenPanSuffix { get; set; }

        /// <summary>
        /// The last few digits (typically four) of the Account PAN.&lt;br&gt;     __Max Length:8__&lt;br&gt; __Required: Yes__ 
        /// </summary>
        /// <value>The last few digits (typically four) of the Account PAN.&lt;br&gt;     __Max Length:8__&lt;br&gt; __Required: Yes__ </value>
        [DataMember(Name="accountPanSuffix", EmitDefaultValue=false)]
        public string AccountPanSuffix { get; set; }

        /// <summary>
        /// The expiry of the Token PAN, given in MMYY format.&lt;br&gt;     __Max Length:4__&lt;br&gt; __Required: Yes__ 
        /// </summary>
        /// <value>The expiry of the Token PAN, given in MMYY format.&lt;br&gt;     __Max Length:4__&lt;br&gt; __Required: Yes__ </value>
        [DataMember(Name="tokenExpiry", EmitDefaultValue=false)]
        public string TokenExpiry { get; set; }

        /// <summary>
        /// The expiry of the Account PAN, given in MMYY format. &lt;br&gt; __Max Length: 4__&lt;br&gt; __Required: No__ 
        /// </summary>
        /// <value>The expiry of the Account PAN, given in MMYY format. &lt;br&gt; __Max Length: 4__&lt;br&gt; __Required: No__ </value>
        [DataMember(Name="accountPanExpiry", EmitDefaultValue=false)]
        public string AccountPanExpiry { get; set; }

        /// <summary>
        /// Whether DSRP transactions are supported by this Token. Must be either &#39;true&#39; (DSRP capable) or &#39;false&#39; (Not DSRP capable).&lt;br&gt; __Max Length: 5__&lt;br&gt; __Required: Yes__ 
        /// </summary>
        /// <value>Whether DSRP transactions are supported by this Token. Must be either &#39;true&#39; (DSRP capable) or &#39;false&#39; (Not DSRP capable).&lt;br&gt; __Max Length: 5__&lt;br&gt; __Required: Yes__ </value>
        [DataMember(Name="dsrpCapable", EmitDefaultValue=false)]
        public string DsrpCapable { get; set; }

        /// <summary>
        /// A value indicating the confidence level of the token to Account PAN binding.&lt;br&gt;     __Max Length:2__&lt;br&gt; __Required: No__ 
        /// </summary>
        /// <value>A value indicating the confidence level of the token to Account PAN binding.&lt;br&gt;     __Max Length:2__&lt;br&gt; __Required: No__ </value>
        [DataMember(Name="tokenAssuranceLevel", EmitDefaultValue=false)]
        public string TokenAssuranceLevel { get; set; }

        /// <summary>
        /// The product category of the Account PAN. When supplied will be one of the following values -  * CREDIT * DEBIT * PREPAID * UNKNOWN  __Max Length: 32__&lt;br&gt; __Required: No__ 
        /// </summary>
        /// <value>The product category of the Account PAN. When supplied will be one of the following values -  * CREDIT * DEBIT * PREPAID * UNKNOWN  __Max Length: 32__&lt;br&gt; __Required: No__ </value>
        [DataMember(Name="productCategory", EmitDefaultValue=false)]
        public string ProductCategory { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class TokenInfo {\n");
            sb.Append("  TokenPanSuffix: ").Append(TokenPanSuffix).Append("\n");
            sb.Append("  AccountPanSuffix: ").Append(AccountPanSuffix).Append("\n");
            sb.Append("  TokenExpiry: ").Append(TokenExpiry).Append("\n");
            sb.Append("  AccountPanExpiry: ").Append(AccountPanExpiry).Append("\n");
            sb.Append("  DsrpCapable: ").Append(DsrpCapable).Append("\n");
            sb.Append("  TokenAssuranceLevel: ").Append(TokenAssuranceLevel).Append("\n");
            sb.Append("  ProductCategory: ").Append(ProductCategory).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as TokenInfo);
        }

        /// <summary>
        /// Returns true if TokenInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of TokenInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(TokenInfo input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.TokenPanSuffix == input.TokenPanSuffix ||
                    (this.TokenPanSuffix != null &&
                    this.TokenPanSuffix.Equals(input.TokenPanSuffix))
                ) && 
                (
                    this.AccountPanSuffix == input.AccountPanSuffix ||
                    (this.AccountPanSuffix != null &&
                    this.AccountPanSuffix.Equals(input.AccountPanSuffix))
                ) && 
                (
                    this.TokenExpiry == input.TokenExpiry ||
                    (this.TokenExpiry != null &&
                    this.TokenExpiry.Equals(input.TokenExpiry))
                ) && 
                (
                    this.AccountPanExpiry == input.AccountPanExpiry ||
                    (this.AccountPanExpiry != null &&
                    this.AccountPanExpiry.Equals(input.AccountPanExpiry))
                ) && 
                (
                    this.DsrpCapable == input.DsrpCapable ||
                    (this.DsrpCapable != null &&
                    this.DsrpCapable.Equals(input.DsrpCapable))
                ) && 
                (
                    this.TokenAssuranceLevel == input.TokenAssuranceLevel ||
                    (this.TokenAssuranceLevel != null &&
                    this.TokenAssuranceLevel.Equals(input.TokenAssuranceLevel))
                ) && 
                (
                    this.ProductCategory == input.ProductCategory ||
                    (this.ProductCategory != null &&
                    this.ProductCategory.Equals(input.ProductCategory))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.TokenPanSuffix != null)
                    hashCode = hashCode * 59 + this.TokenPanSuffix.GetHashCode();
                if (this.AccountPanSuffix != null)
                    hashCode = hashCode * 59 + this.AccountPanSuffix.GetHashCode();
                if (this.TokenExpiry != null)
                    hashCode = hashCode * 59 + this.TokenExpiry.GetHashCode();
                if (this.AccountPanExpiry != null)
                    hashCode = hashCode * 59 + this.AccountPanExpiry.GetHashCode();
                if (this.DsrpCapable != null)
                    hashCode = hashCode * 59 + this.DsrpCapable.GetHashCode();
                if (this.TokenAssuranceLevel != null)
                    hashCode = hashCode * 59 + this.TokenAssuranceLevel.GetHashCode();
                if (this.ProductCategory != null)
                    hashCode = hashCode * 59 + this.ProductCategory.GetHashCode();
                return hashCode;
            }
        }
    }

}
