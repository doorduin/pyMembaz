#Implement a simple interface for getting data in and out of membaz
#NB remove defaults
DEFAULT_user = None
DEFAULT_password = None

#Membaz WSDL detail:
""" Prefixes:
     xsd: http://www.w3.org/2001/XMLSchema
     ns0: https://www.membaz.com/ws/MembershipService.asmx

Global elements:

     ns0:AddMember(memberPost: ns0:MemberPost)
     ns0:AddMemberResponse(AddMemberResult: xsd:string)
     ns0:DownloadAttachment(membershipNumber: xsd:string, attachmentTypeId: xsd:int)
     ns0:DownloadAttachmentResponse(DownloadAttachmentResult: xsd:base64Binary)
     ns0:UpdateMember(memberPost: ns0:MemberPost)
     ns0:UpdateMemberResponse()
     ns0:UploadAttachment(membershipNumber: xsd:string, attachmentTypeId: xsd:int, attachmentContent: xsd:base64Binary, friendlyName: xsd:string)
     ns0:UploadAttachmentResponse()
     ns0:ViewAttachmentTypes()
     ns0:ViewAttachmentTypesResponse(ViewAttachmentTypesResult: ns0:ViewAttachmentTypeResult)
     ns0:ViewCategories()
     ns0:ViewCategoriesResponse(ViewCategoriesResult: ns0:ViewCategoriesResult)
     ns0:ViewCustomFields()
     ns0:ViewCustomFieldsResponse(ViewCustomFieldsResult: ns0:ViewCustomFieldsResult)
     ns0:ViewMember(membershipNumber: xsd:string)
     ns0:ViewMemberResponse(ViewMemberResult: ns0:ViewMemberResult)
     ns0:ViewMembers(searchString: xsd:string)
     ns0:ViewMembersResponse(ViewMembersResult: ns0:ViewMembersResult)
     ns0:ViewMembersWithSorting(searchString: xsd:string, sortOrder: xsd:string)
     ns0:ViewMembersWithSortingAndPaging(searchString: xsd:string, sortOrder: xsd:string, startRowIndex: xsd:int, pageSize: xsd:int)
     ns0:ViewMembersWithSortingAndPagingResponse(ViewMembersWithSortingAndPagingResult: ns0:ViewMembersResult)
     ns0:ViewMembersWithSortingResponse(ViewMembersWithSortingResult: ns0:ViewMembersResult)

Global types:
     xsd:anyType
     xsd:ENTITIES
     xsd:ENTITY
     xsd:ID
     xsd:IDREF
     xsd:IDREFS
     xsd:NCName
     xsd:NMTOKEN
     xsd:NMTOKENS
     xsd:NOTATION
     xsd:Name
     xsd:QName
     xsd:anySimpleType
     xsd:anyURI
     xsd:base64Binary
     xsd:boolean
     xsd:byte
     xsd:date
     xsd:dateTime
     xsd:decimal
     xsd:double
     xsd:duration
     xsd:float
     xsd:gDay
     xsd:gMonth
     xsd:gMonthDay
     xsd:gYear
     xsd:gYearMonth
     xsd:hexBinary
     xsd:int
     xsd:integer
     xsd:language
     xsd:long
     xsd:negativeInteger
     xsd:nonNegativeInteger
     xsd:nonPositiveInteger
     xsd:normalizedString
     xsd:positiveInteger
     xsd:short
     xsd:string
     xsd:time
     xsd:token
     xsd:unsignedByte
     xsd:unsignedInt
     xsd:unsignedLong
     xsd:unsignedShort
     ns0:ArrayOfAttachmentType(AttachmentType: ns0:AttachmentType[])
     ns0:ArrayOfCategory(Category: ns0:Category[])
     ns0:ArrayOfCustomField(CustomField: ns0:CustomField[])
     ns0:ArrayOfMemberAttachment(MemberAttachment: ns0:MemberAttachment[])
     ns0:ArrayOfMemberCategory(MemberCategory: ns0:MemberCategory[])
     ns0:ArrayOfMemberCategoryPost(MemberCategoryPost: ns0:MemberCategoryPost[])
     ns0:ArrayOfMemberCustomField(MemberCustomField: ns0:MemberCustomField[])
     ns0:ArrayOfMemberCustomFieldPost(MemberCustomFieldPost: ns0:MemberCustomFieldPost[])
     ns0:ArrayOfViewMemberResult(ViewMemberResult: ns0:ViewMemberResult[])
     ns0:AttachmentType(AttachmentTypeId: xsd:int, AttachmentTypeName: xsd:string)
     ns0:Category(CategoryId: xsd:int, CategoryName: xsd:string)
     ns0:CustomField(CustomFieldId: xsd:int, CustomFieldName: xsd:string)
     ns0:GenderEnum
     ns0:MemberAddress(AddressLine1: xsd:string, AddressLine2: xsd:string, AddressLine3: xsd:string, AddressLine4: xsd:string, AddressCode: xsd:string)
     ns0:MemberAddressPost(AddressLine1: xsd:string, AddressLine2: xsd:string, AddressLine3: xsd:string, AddressLine4: xsd:string, AddressCode: xsd:string)
     ns0:MemberAttachment(AttachmentTypeId: xsd:int, AttachmentTypeName: xsd:string, AttachmentFilename: xsd:string)
     ns0:MemberCategory(CategoryId: xsd:int, CategoryName: xsd:string, CategoryValue: xsd:boolean)
     ns0:MemberCategoryPost(CategoryId: xsd:int, CategoryValue: xsd:boolean)
     ns0:MemberCustomField(CustomFieldId: xsd:int, CustomFieldName: xsd:string, CustomFieldValue: xsd:string)
     ns0:MemberCustomFieldPost(CustomFieldId: xsd:int, CustomFieldValue: xsd:string)
     ns0:MemberPhone(ContactPerson: xsd:string, CountryCode: xsd:string, AreaCode: xsd:string, PhoneNumber: xsd:string)
     ns0:MemberPhonePost(ContactPerson: xsd:string, CountryCode: xsd:string, AreaCode: xsd:string, PhoneNumber: xsd:string)
     ns0:MemberPost(MembershipNumber: xsd:string, Title: xsd:string, FirstName: xsd:string, LastName: xsd:string, KnownAs: xsd:string, Email: xsd:string, JoinedDate: xsd:dateTime, Gender: ns0:GenderEnum, Birthdate: xsd:dateTime, Memo: xsd:string, TaxReferenceNumber: xsd:string, MembershipExpiryDate: xsd:dateTime, WebsiteUrl: xsd:string, Company: xsd:string, Position: xsd:string, MemberCustomFields: ns0:ArrayOfMemberCustomFieldPost, MemberCategories: ns0:ArrayOfMemberCategoryPost, CellNumber: ns0:MemberPhonePost, FaxNumber: ns0:MemberPhonePost, HomePhoneNumber: ns0:MemberPhonePost, OfficeNumber: ns0:MemberPhonePost, PhysicalAddress: ns0:MemberAddressPost, PostalAddress: ns0:MemberAddressPost)
     ns0:ViewAttachmentTypeResult(AttachmentTypes: ns0:ArrayOfAttachmentType)
     ns0:ViewCategoriesResult(Categories: ns0:ArrayOfCategory)
     ns0:ViewCustomFieldsResult(CustomFields: ns0:ArrayOfCustomField)
     ns0:ViewMemberResult(MembershipNumber: xsd:string, Title: xsd:string, FirstName: xsd:string, LastName: xsd:string, Email: xsd:string, JoinedDate: xsd:dateTime, Gender: xsd:string, Birthdate: xsd:dateTime, OpeningBalance: xsd:double, Adjustments: xsd:double, Paid: xsd:double, Fees: xsd:double, CurrentBalance: xsd:double, PointBalance: xsd:double, Memo: xsd:string, TaxReferenceNumber: xsd:string, MembershipExpiryDate: xsd:dateTime, WebsiteUrl: xsd:string, Company: xsd:string, Position: xsd:string, Age: xsd:string, CellNumber: ns0:MemberPhone, FaxNumber: ns0:MemberPhone, HomePhoneNumber: ns0:MemberPhone, OfficeNumber: ns0:MemberPhone, PhysicalAddress: ns0:MemberAddress, PostalAddress: ns0:MemberAddress, MemberCategories: ns0:ArrayOfMemberCategory, MemberCustomFields: ns0:ArrayOfMemberCustomField, MemberAttachments: ns0:ArrayOfMemberAttachment)
     ns0:ViewMembersResult(Members: ns0:ArrayOfViewMemberResult)

Bindings:
     Soap11Binding: {https://www.membaz.com/ws/MembershipService.asmx}MembershipServiceSoap
     Soap12Binding: {https://www.membaz.com/ws/MembershipService.asmx}MembershipServiceSoap12

Service: MembershipService
     Port: MembershipServiceSoap (Soap11Binding: {https://www.membaz.com/ws/MembershipService.asmx}MembershipServiceSoap)
         Operations:
            AddMember(memberPost: ns0:MemberPost) -> AddMemberResult: xsd:string
            DownloadAttachment(membershipNumber: xsd:string, attachmentTypeId: xsd:int) -> DownloadAttachmentResult: xsd:base64Binary
            UpdateMember(memberPost: ns0:MemberPost) ->
            UploadAttachment(membershipNumber: xsd:string, attachmentTypeId: xsd:int, attachmentContent: xsd:base64Binary, friendlyName: xsd:string) ->
            ViewAttachmentTypes() -> ViewAttachmentTypesResult: ns0:ViewAttachmentTypeResult
            ViewCategories() -> ViewCategoriesResult: ns0:ViewCategoriesResult
            ViewCustomFields() -> ViewCustomFieldsResult: ns0:ViewCustomFieldsResult
            ViewMember(membershipNumber: xsd:string) -> ViewMemberResult: ns0:ViewMemberResult
            ViewMembers(searchString: xsd:string) -> ViewMembersResult: ns0:ViewMembersResult
            ViewMembersWithSorting(searchString: xsd:string, sortOrder: xsd:string) -> ViewMembersWithSortingResult: ns0:ViewMembersResult
            ViewMembersWithSortingAndPaging(searchString: xsd:string, sortOrder: xsd:string, startRowIndex: xsd:int, pageSize: xsd:int) -> ViewMembersWithSortingAndPagingResult: ns0:ViewMembersResult

     Port: MembershipServiceSoap12 (Soap12Binding: {https://www.membaz.com/ws/MembershipService.asmx}MembershipServiceSoap12)
         Operations:
            AddMember(memberPost: ns0:MemberPost) -> AddMemberResult: xsd:string
            DownloadAttachment(membershipNumber: xsd:string, attachmentTypeId: xsd:int) -> DownloadAttachmentResult: xsd:base64Binary
            UpdateMember(memberPost: ns0:MemberPost) ->
            UploadAttachment(membershipNumber: xsd:string, attachmentTypeId: xsd:int, attachmentContent: xsd:base64Binary, friendlyName: xsd:string) ->
            ViewAttachmentTypes() -> ViewAttachmentTypesResult: ns0:ViewAttachmentTypeResult
            ViewCategories() -> ViewCategoriesResult: ns0:ViewCategoriesResult
            ViewCustomFields() -> ViewCustomFieldsResult: ns0:ViewCustomFieldsResult
            ViewMember(membershipNumber: xsd:string) -> ViewMemberResult: ns0:ViewMemberResult
            ViewMembers(searchString: xsd:string) -> ViewMembersResult: ns0:ViewMembersResult
            ViewMembersWithSorting(searchString: xsd:string, sortOrder: xsd:string) -> ViewMembersWithSortingResult: ns0:ViewMembersResult
            ViewMembersWithSortingAndPaging(searchString: xsd:string, sortOrder: xsd:string, startRowIndex: xsd:int, pageSize: xsd:int) -> ViewMembersWithSortingAndPagingResult: ns0:ViewMembersResult
 """

import logging.config

from zeep import Client, Settings, xsd, exceptions
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep.transports import Transport

class Membaz:
    def __init__(self,url=None,user=None, password=None):
        if url is None:
            print ("Get URL from Membaz")
            return
        self.user = None
        self.password = None
        self.setUser(user)
        self.setPassword(password)

        # set the WSDL URL
        self.wsdl_url = url+"/membershipservice.asmx?WSDL"
        
        # set method URL
        self.method_url = url+"/membershipservice.asmx"
        
        # set service URL
        self.service_url = url+"/membershipservice.asmx"
        
        #https://www.membaz.com/api/MemberCard/48/PAA1/7d4efbb2-f4f2-47ad-982c-e8f0e7
        #https://www.membaz.com/api/48/7d4efbb2-f4f2-47ad-982c-e8f0e7

        logging.config.dictConfig({
            'version': 1,
            'formatters': {
                'verbose': {
                    'format': '%(name)s: %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'level': 'INFO',
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose',
                },
            },
            'loggers': {
                'zeep.transports': {
                    'level': 'ERROR',
                    'propagate': True,
                    'handlers': ['console'],
                },
            }
        })

        # create the header element
        self.header = xsd.Element(
            "Header",
            xsd.ComplexType(
                [
                    xsd.Element(
                        "{http://www.w3.org/2005/08/addressing}Action", xsd.String()
                    ),
                    xsd.Element(
                        "{http://www.w3.org/2005/08/addressing}To", xsd.String()
                    ),
                ]
            ),
        )

        # set the header value from header element
        self.header_value = self.header(Action=self.method_url, To=self.service_url)
    
    def setUser(self,user = None):
        if user is None:
            self.user = DEFAULT_user
        else:
            self.user = user
        if self.password is None:
            return
        self.header_credentials = {'username':self.user,'password':self.password}

    def setPassword(self,password=None):
        if password is None:
            self.password = DEFAULT_password
        else:
            self.password = password
        if self.user is None:
            return
        self.header_credentials = {'username':self.user,'password':self.password}

    def open(self,user=None,password=None):
        self.setUser(user)
        self.setPassword(password)

        self.session = Session()
        self.session.auth = HTTPBasicAuth(self.user, self.password)

        # initialize zeep client
        self.settings = Settings(strict=False, xml_huge_tree=True)
        self.client = Client(wsdl=self.wsdl_url,settings=self.settings,transport=Transport(session=self.session))
        self.client.bind('MembershipService','MembershipServiceSoap12')

    def readMembersData(self, memberShipNo, verbose=False):
        if verbose:
            print ('Membership no:' ,memberShipNo) 
        with self.client.settings(raw_response=False):
            try:
                response = self.client.service.ViewMember(
                    membershipNumber=memberShipNo,
                    _soapheaders=[self.header_value]
                )
                return response
            except exceptions.Fault as e:
                if verbose:         
                    print (e)
                return None
        return None

    def packMembersData(self, response,verbose=False, csv=False):

        """
        ns0:MemberPost(
            MembershipNumber: xsd:string,
            Title: xsd:string,
            FirstName: xsd:string,
            LastName: xsd:string,
            KnownAs: xsd:string,
            Email: xsd:string,
            JoinedDate: xsd:dateTime,
            Gender: ns0:GenderEnum, 
            Birthdate: xsd:dateTime, 
            Memo: xsd:string, 
            TaxReferenceNumber: xsd:string, 
            MembershipExpiryDate: xsd:dateTime, 
            WebsiteUrl: xsd:string, 
            Company: xsd:string, 
            Position: xsd:string, 
            MemberCustomFields: ns0:ArrayOfMemberCustomFieldPost, 
            MemberCategories: ns0:ArrayOfMemberCategoryPost, 
                ns0:ArrayOfMemberCategoryPost(MemberCategoryPost: ns0:MemberCategoryPost[
                    ns0:MemberCategoryPost(CategoryId: xsd:int, CategoryValue: xsd:boolean)
                ])
            CellNumber: ns0:MemberPhonePost, 
            FaxNumber: ns0:MemberPhonePost, 
            HomePhoneNumber: ns0:MemberPhonePost, 
            OfficeNumber: ns0:MemberPhonePost, 
            PhysicalAddress: ns0:MemberAddressPost, 
            PostalAddress: ns0:MemberAddressPost)
        """

        #Datastructure Types
        member_type = self.client.get_type('ns0:MemberPost')
        CellNumber_type = self.client.get_type('ns0:MemberPhone')
        FaxNumber_type = self.client.get_type('ns0:MemberPhone')
        HomePhoneNumber_type = self.client.get_type('ns0:MemberPhone')
        OfficeNumber_type = self.client.get_type('ns0:MemberPhone')
        PhysicalAddress_type = self.client.get_type('ns0:MemberAddress')
        PostalAddress_type = self.client.get_type('ns0:MemberAddress')
        MemberCategories_type = self.client.get_type('ns0:ArrayOfMemberCategory')
        MemberCategory_type = self.client.get_type('ns0:MemberCategory')
        MemberCustomField_type = self.client.get_type('ns0:ArrayOfMemberCustomField')
        MemberCustomFieldPost_type = self.client.get_type('ns0:MemberCustomField')

        #Pack the defaults
        if verbose:
            for theKey in response:
                print(theKey, '->', response[theKey])
                #if response[theKey] is not None:
                #    theValue = response[theKey]

        #Prep deeper fields:
        cellNumber = CellNumber_type(
            ContactPerson=response['CellNumber']['ContactPerson'],
            CountryCode=response['CellNumber']['CountryCode'],
            AreaCode=response['CellNumber']['AreaCode'],
            PhoneNumber=response['CellNumber']['PhoneNumber']
        )
        faxNumber = FaxNumber_type(
            ContactPerson=response['FaxNumber']['ContactPerson'],
            CountryCode=response['FaxNumber']['CountryCode'],
            AreaCode=response['FaxNumber']['AreaCode'],
            PhoneNumber=response['FaxNumber']['PhoneNumber']
        )
        homePhoneNumber = HomePhoneNumber_type(
            ContactPerson=response['HomePhoneNumber']['ContactPerson'],
            CountryCode=response['HomePhoneNumber']['CountryCode'],
            AreaCode=response['HomePhoneNumber']['AreaCode'],
            PhoneNumber=response['HomePhoneNumber']['PhoneNumber']
        )
        officeNumber = OfficeNumber_type(
            ContactPerson=response['OfficeNumber']['ContactPerson'],
            CountryCode=response['OfficeNumber']['CountryCode'],
            AreaCode=response['OfficeNumber']['AreaCode'],
            PhoneNumber=response['OfficeNumber']['PhoneNumber']
        )
        physicalAddress = PhysicalAddress_type(
            AddressLine1=response['PhysicalAddress']['AddressLine1'],
            AddressLine2=response['PhysicalAddress']['AddressLine2'],
            AddressLine3=response['PhysicalAddress']['AddressLine3'],
            AddressLine4=response['PhysicalAddress']['AddressLine4'],
            AddressCode=response['PhysicalAddress']['AddressCode']
        )
        postalAddress = PostalAddress_type(
            AddressLine1=response['PostalAddress']['AddressLine1'],
            AddressLine2=response['PostalAddress']['AddressLine2'],
            AddressLine3=response['PostalAddress']['AddressLine3'],
            AddressLine4=response['PostalAddress']['AddressLine4'],
            AddressCode=response['PostalAddress']['AddressCode']
        )

        #Membership Catergories
        if (True):
            theList = []
            #theMembershipCatagoryFieldsList = self.listMemberCategoryDictList(response,theList)
            #print(theMembershipCatagoryFieldsList)
            #Only add valid / true fields
            memberCustomCategories = []
            for field in response['MemberCategories']['MemberCategory']:
                memberCustomCategories.append(field)
            #for fieldCategoryID in theMembershipCatagoryFieldsList:
            #    memberCategories.append(MemberCategory_type(
            #        CategoryId = fieldCategoryID,
            #        CategoryFieldName = None,
            #        CategoryValue = True))
        else:
            memberCategories = response['MemberCategories']['MemberCategory']
        memberCategories = MemberCategories_type(
            MemberCategory=memberCustomCategories
        )
        if verbose:
            print(memberCategories)

        #MemberCustomFields
        if (True):
            #theDictionary = self.listMemberCustomFields(response)
            #print(theDictionary)
            #Only add valid / true fields
            memberCustomFields = []
            for field in response['MemberCustomFields']['MemberCustomField']:
                if field['CustomFieldValue'] is not None:
                    if field['CustomFieldValue'] == 'NA':
                        pass
                    else:
                        memberCustomFields.append(field)
        else:
            memberCustomFields = response['MemberCustomFields']['MemberCustomField']
        if memberCustomFields is not None:
            memberCustomFields = MemberCustomField_type(
                MemberCustomField=memberCustomFields
            )
        if (verbose):
            print(memberCustomFields)

        if response['Position'] is None:
            response['Position'] = "NA"

        #Combine all fields data
        memberPost = member_type(
            MembershipNumber= response['MembershipNumber'],
            Title = response['Title'],
            FirstName = response['FirstName'],
            LastName = response['LastName'],
            KnownAs = response['KnownAs'],
            Email = response['Email'],
            JoinedDate = response['JoinedDate'],
            Gender = response['Gender'],
            Birthdate = response['Birthdate'],
            Memo = response['Memo'],
            TaxReferenceNumber = response['TaxReferenceNumber'],
            MembershipExpiryDate = response['MembershipExpiryDate'],
            WebsiteUrl = response['WebsiteUrl'],
            Company = response['Company'],
            Position = response['Position'],
            MemberCategories = memberCategories,
            MemberCustomFields = memberCustomFields,
            CellNumber = cellNumber,
            FaxNumber = faxNumber,
            HomePhoneNumber = homePhoneNumber,
            OfficeNumber = officeNumber,
            PhysicalAddress = physicalAddress,
            PostalAddress = postalAddress
        )
        if verbose:
            print(memberPost)
        return memberPost

    def uploadMembersData(self, memberPost=None, verbose=False):
        """
        UpdateMember(memberPost: ns0:MemberPost)
        """
        if memberPost is None:
            print ("No memberPost given!!!")
            return None
        if verbose:
            #print ('Membership no:' ,memberShipNo) 
            pass
        with self.client.settings(raw_response=False):
            try:
                response = self.client.service.UpdateMember(
                    memberPost=memberPost,
                    _soapheaders=[self.header_value]
                )
                return response
            except exceptions.Fault as e:
                if verbose:       
                    print (e)
                    print ("E"*80)
                    #print (memberPost)
                    #print ("e"*80)
                return None
        return None

    def readAttachementTypes(self, verbose=False):
        with self.client.settings(raw_response=False):
            try:
                response = self.client.service.ViewAttachmentTypes(
                    _soapheaders=[self.header_value]
                )
                return response
            except exceptions.Fault as e:
                if verbose:         
                    print (e)
                return None
        return None

    def downloadMembersImage(self, memberShipNo, verbose=False):
        if verbose:
            print ('Membership no:' ,memberShipNo) 
        with self.client.settings(raw_response=False):
            try:
                response = self.client.service.DownloadMemberImage(
                    membershipNumber=memberShipNo,
                    _soapheaders=[self.header_value]
                )
                return response
            except exceptions.Fault as e:
                if verbose:         
                    print (e)
                return None
        return None

    def uploadMembersImage(self, memberShipNo, theFile=None, verbose=False):
        if theFile is None:
            print ("No File given!!! Please include file")
            return None
        if verbose:
            print ('Membership no:' ,memberShipNo) 
        with self.client.settings(raw_response=False):
            try:
                response = self.client.service.UploadMemberImage(
                    membershipNumber=memberShipNo,
                    memberImage=theFile,
                    _soapheaders=[self.header_value]
                )
                return response
            except exceptions.Fault as e:
                if verbose:         
                    print (e)
                return None
        return None

    ## Helper Functions
    def returnMemberCustomFields(self, memberResponse, fieldName):
        try:
            for res in memberResponse['MemberCustomFields']['MemberCustomField']:
                if res['CustomFieldName'] == fieldName:
                    return res['CustomFieldValue']
        except:
            return None

    def returnMemberCategoryFields(self,memberResponse, membershipCategory):
        try:
            for res in memberResponse['MemberCategories']['MemberCategory']:
                if res['CategoryName'] == membershipCategory:
                    return res['CategoryValue']
        except:
            return None

    def returnMemberCategoryId(self,memberResponse, membershipCategory):
        try:
            for res in memberResponse['MemberCategories']['MemberCategory']:
                if res['CategoryName'] == membershipCategory:
                    return res['CategoryId']
        except:
            return None

    def listMemberCategoryIds(self,memberResponse, theList=[]):
        try:
            for res in memberResponse['MemberCategories']['MemberCategory']:
                if res['CategoryValue']:
                    theList.append(res['CategoryId'])
        except:
            pass
        return theList
    
    def categoryToDict(self, memberResponse, category='MemberCategory', theDict={}):
        try:
            for res in memberResponse['MemberCategories'][category]:
                if res['CategoryValue']:                 
                    theDict[res['CategoryGroupName']] = res['CategoryName']
        except:
            pass
        return theDict

    def listMemberCustomFields(self,memberResponse, theDict={}):
        try:
            for res in memberResponse['MemberCustomFields']['MemberCustomField']:
                if res['CustomFieldValue'] is not None:
                    theDict[res['CustomFieldId']] = res['CustomFieldValue']
        except:
            pass
        return theDict    

    def customFieldsToDict(self, memberResponse, category='MemberCustomField', theDict={}):
        try:
            for res in memberResponse['MemberCustomFields'][category]:
                if res['CustomFieldValue'] is not None:                 
                    theDict[res['CustomFieldName']] = res['CustomFieldValue']
        except:
            pass
        return theDict
    
    def setMemberCategoryTrue(self, memberResponse, categoryGroupName, categoryName):
        try:
            theLen = len(memberResponse['MemberCategories']['MemberCategory'])
            for i in range(theLen):
                res = memberResponse['MemberCategories']['MemberCategory'][i]
                if res['CategoryGroupName'].upper() == categoryGroupName.upper():
                    if res['CategoryName'].upper() == categoryName.upper():
                        memberResponse['MemberCategories']['MemberCategory'][i]['CategoryValue'] = True
                    else:
                        memberResponse['MemberCategories']['MemberCategory'][i]['CategoryValue'] = False
        except:
            pass
        return memberResponse        
    
def doMain():
    print ("Dont run it here....")
 
if __name__ == "__main__":
	#doMain()
    pass