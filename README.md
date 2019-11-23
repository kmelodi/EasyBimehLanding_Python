# Getting started

EasyBimehConnect 

 یک ساب برند از ایزی بیمه است که وظیفه ارائه خدمات

 B2B و B2B2C

را برپایه وب سرویس و وایت لیبل بر عهده دارد. اگر اپلیکیشن و یا سایت غیر بیمه‌ای دارید و تمایل به فروش بیمه نامه دارید از امروز میتوانید با کمترین هزینه و کمترین زمان به زنجیره نوآوری در صنعت بیمه متصل شوید و تجارت جدیدی بسازید

به دلیل گستردگی پروژه و برای دسترسی بهتر، این پروژه به بخش های مختلف تقسیم شده است

و هر بخش در 10 پلتفرم مختلف، ارایه شده است

در این بخش، به وب سرویس های مربوط به صفحه ی لندینگ مرکز بیمه، دسترسی خواهید داشت که 

اطلاعات هر پلتفرم را میتوانید بصورت تجمیعی در آدرس زیر مشاهده نمایید

https://www.apimatic.io/apidocs/easybimehlanding

و یا بصورت مجزا در آدرس های زیر قابل درسترس می باشند

1- Android: https://github.com/kmelodi/EasyBimehLanding_Android

2- .Net: https://github.com/kmelodi/EasyBimehLanding_.NET

3- Ios: https://github.com/kmelodi/EasyBimehLanding_IOS

4- Java: https://github.com/kmelodi/EasyBimehLanding_JAVA

5- Php: https://github.com/kmelodi/EasyBimehLanding_PHP

6- Python: https://github.com/kmelodi/EasyBimehLanding_Python

7- Ruby: https://github.com/kmelodi/EasyBimehLanding_Ruby

8- Angular: https://github.com/kmelodi/EasyBimehLanding_Angular

9- NodeJs: https://github.com/kmelodi/EasyBimehLanding_NodeJs

10- Go: https://github.com/kmelodi/EasyBimehLanding_Go


برای اطلاعات بیشتر به آدرس زیر مراجعه نمایید

https://easybimeh.com/ebconnect

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Easy%20Bimeh%20Landing-Python)


## How to Use

The following section explains how to use the Easybimehlanding SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Easy%20Bimeh%20Landing-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Easy%20Bimeh%20Landing-Python&projectName=easybimehlanding)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Easy%20Bimeh%20Landing-Python&projectName=easybimehlanding)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Easy%20Bimeh%20Landing-Python&projectName=easybimehlanding)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from easybimehlanding.easybimehlanding_client import EasybimehlandingClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Easy%20Bimeh%20Landing-Python&libraryName=easybimehlanding.easybimehlanding_client&projectName=easybimehlanding&className=EasybimehlandingClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Easy%20Bimeh%20Landing-Python&libraryName=easybimehlanding.easybimehlanding_client&projectName=easybimehlanding&className=EasybimehlandingClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### 

API client can be initialized as following.

```python

client = EasybimehlandingClient()
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [FileManagerController](#file_manager_controller)
* [LiabilityDoctorInsuranceController](#liability_doctor_insurance_controller)
* [CarBodyController](#car_body_controller)
* [ElectronicEquipmentInsuranceController](#electronic_equipment_insurance_controller)
* [OtherInsuranceTypesController](#other_insurance_types_controller)
* [ThirdPartyInsuranceController](#third_party_insurance_controller)
* [MotorcycleInsuranceController](#motorcycle_insurance_controller)
* [FireInsuranceController](#fire_insurance_controller)
* [EarthquakeInsuranceController](#earthquake_insurance_controller)
* [TravelInsuranceController](#travel_insurance_controller)
* [ElevatorInsuranceController](#elevator_insurance_controller)
* [MainController](#main_controller)
* [ComboDataController](#combo_data_controller)
* [TrackingDamageController](#tracking_damage_controller)
* [FooterController](#footer_controller)
* [InsurancePolicyPlanController](#insurance_policy_plan_controller)

## <a name="file_manager_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FileManagerController") FileManagerController

### Get controller instance

An instance of the ``` FileManagerController ``` class can be accessed from the API Client.

```python
 file_manager_controller = client.file_manager
```

### <a name="upload"></a>![Method: ](https://apidocs.io/img/method.png ".FileManagerController.upload") upload

> آپلود فایل در ایزی بیمه
> بعد از آپلود، ادرس فایل باید در api های بعدی ارسال شود.

```python
def upload(self,
                sub_domain,
                x_api_key,
                file)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |
| file |  ``` Required ```  | فایل ارسالی |



#### Example Usage

```python
sub_domain = 'hfz1'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'
file = 'file'

result = file_manager_controller.upload(sub_domain, x_api_key, file)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="liability_doctor_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LiabilityDoctorInsuranceController") LiabilityDoctorInsuranceController

### Get controller instance

An instance of the ``` LiabilityDoctorInsuranceController ``` class can be accessed from the API Client.

```python
 liability_doctor_insurance_controller = client.liability_doctor_insurance
```

### <a name="get_liability_doctor_insurance"></a>![Method: ](https://apidocs.io/img/method.png ".LiabilityDoctorInsuranceController.get_liability_doctor_insurance") get_liability_doctor_insurance

> در یافت اطلاعات اولیه برای استعلام بیمه مسئولیت پزشکان

```python
def get_liability_doctor_insurance(self,
                                       sub_domain,
                                       x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = liability_doctor_insurance_controller.get_liability_doctor_insurance(sub_domain, x_api_key)

```


### <a name="get_medical_specialties"></a>![Method: ](https://apidocs.io/img/method.png ".LiabilityDoctorInsuranceController.get_medical_specialties") get_medical_specialties

> دریافت لیست تخصص های پزشکی

```python
def get_medical_specialties(self,
                                id,
                                x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | نوع تخصص => ParamedicalExpertise => پیراپزشکی MedicalExpertise => پزشکی |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
id = 'ParamedicalExpertise'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = liability_doctor_insurance_controller.get_medical_specialties(id, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="car_body_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CarBodyController") CarBodyController

### Get controller instance

An instance of the ``` CarBodyController ``` class can be accessed from the API Client.

```python
 car_body_controller = client.car_body
```

### <a name="get_car_brand"></a>![Method: ](https://apidocs.io/img/method.png ".CarBodyController.get_car_brand") get_car_brand

> دریافت برند خودرو

```python
def get_car_brand(self,
                      x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| xApiKey |  ``` Required ```  | شناسه ی اختصاصی ارتباط با سرور |



#### Example Usage

```python
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = car_body_controller.get_car_brand(x_api_key)

```


### <a name="get_car_brand_tips"></a>![Method: ](https://apidocs.io/img/method.png ".CarBodyController.get_car_brand_tips") get_car_brand_tips

> دریافت لیست تیپ خودرو

```python
def get_car_brand_tips(self,
                           car_brand_id,
                           x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| carBrandId |  ``` Required ```  | شناسه ی برند خودرو |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
car_brand_id = 190
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = car_body_controller.get_car_brand_tips(car_brand_id, x_api_key)

```


### <a name="get_has_plan"></a>![Method: ](https://apidocs.io/img/method.png ".CarBodyController.get_has_plan") get_has_plan

> آیا این نوع بیمه نامه، طرح بیمه ای دارد؟

```python
def get_has_plan(self,
                     sub_domain,
                     insurance_policy_type,
                     x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insurancePolicyType |  ``` Required ```  | شناسه ی نوع بیمه نامه => بیمه بدنه=2 |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_policy_type = 2
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = car_body_controller.get_has_plan(sub_domain, insurance_policy_type, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="electronic_equipment_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ElectronicEquipmentInsuranceController") ElectronicEquipmentInsuranceController

### Get controller instance

An instance of the ``` ElectronicEquipmentInsuranceController ``` class can be accessed from the API Client.

```python
 electronic_equipment_insurance_controller = client.electronic_equipment_insurance
```

### <a name="get_electronic_equipment_insurance"></a>![Method: ](https://apidocs.io/img/method.png ".ElectronicEquipmentInsuranceController.get_electronic_equipment_insurance") get_electronic_equipment_insurance

> دریافت اطلاعات اولیه استعلام بیمه نامه ی تجهیزات الکترونیک

```python
def get_electronic_equipment_insurance(self,
                                           sub_domain,
                                           x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'subDomain'
x_api_key = 'x-api-key'

result = electronic_equipment_insurance_controller.get_electronic_equipment_insurance(sub_domain, x_api_key)

```


### <a name="get_device_brand_types"></a>![Method: ](https://apidocs.io/img/method.png ".ElectronicEquipmentInsuranceController.get_device_brand_types") get_device_brand_types

> دریافت لیست نوع برند دستگاه

```python
def get_device_brand_types(self,
                               device_group,
                               device_type_id,
                               x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| deviceGroup |  ``` Required ```  | شناسه ی گروه دستگاه |
| deviceTypeId |  ``` Required ```  | شناسه ی نوع دستگاه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
device_group = 1
device_type_id = 1
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = electronic_equipment_insurance_controller.get_device_brand_types(device_group, device_type_id, x_api_key)

```


### <a name="get_divice_franchisee"></a>![Method: ](https://apidocs.io/img/method.png ".ElectronicEquipmentInsuranceController.get_divice_franchisee") get_divice_franchisee

> دریافت لیست فرانشیر استعلام بیمه نامه ی تجهیزات الکترونیک

```python
def get_divice_franchisee(self,
                              device_model_id,
                              x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| deviceModelId |  ``` Required ```  | شناسه ی مدل دستگاه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
device_model_id = 1340
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = electronic_equipment_insurance_controller.get_divice_franchisee(device_model_id, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="other_insurance_types_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OtherInsuranceTypesController") OtherInsuranceTypesController

### Get controller instance

An instance of the ``` OtherInsuranceTypesController ``` class can be accessed from the API Client.

```python
 other_insurance_types_controller = client.other_insurance_types
```

### <a name="get_other_insurance_types"></a>![Method: ](https://apidocs.io/img/method.png ".OtherInsuranceTypesController.get_other_insurance_types") get_other_insurance_types

> دریافت لیست سایر بیمه نامه ها

```python
def get_other_insurance_types(self,
                                  sub_domain,
                                  x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = other_insurance_types_controller.get_other_insurance_types(sub_domain, x_api_key)

```


### <a name="get_send_sms_token"></a>![Method: ](https://apidocs.io/img/method.png ".OtherInsuranceTypesController.get_send_sms_token") get_send_sms_token

> ارسال توکن تایید شماره تماس، برای احراز هویت کاربر

```python
def get_send_sms_token(self,
                           mobile,
                           insurance_centre_sub_domain,
                           x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mobile |  ``` Required ```  | شماره موبایل |
| insuranceCentreSubDomain |  ``` Required ```  | دامنه یا زیردامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
mobile = '09018318086'
insurance_centre_sub_domain = 'hfz1'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = other_insurance_types_controller.get_send_sms_token(mobile, insurance_centre_sub_domain, x_api_key)

```


### <a name="get_verify_sms_token"></a>![Method: ](https://apidocs.io/img/method.png ".OtherInsuranceTypesController.get_verify_sms_token") get_verify_sms_token

> تایید توکن پیامک شده به کاربر، برای احراز هویت

```python
def get_verify_sms_token(self,
                             mobile,
                             token,
                             insurance_centre_sub_domain,
                             alias_name,
                             resource,
                             x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mobile |  ``` Required ```  | شماره موبایل |
| token |  ``` Required ```  | توکن دریافتی کاربر از پیامک |
| insuranceCentreSubDomain |  ``` Required ```  | دامنه یا زیر دامنه ی اختصاصی مرکز بیمه |
| aliasName |  ``` Required ```  | نام و نام خانوادگی کاربر |
| resource |  ``` Required ```  | دامنه ی درخواست دهنده |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
mobile = '09018318086'
token = 27763
insurance_centre_sub_domain = 'hfz1'
alias_name = 'علی موسوی'
resource = 'https://hfz1.easybimeh.com'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = other_insurance_types_controller.get_verify_sms_token(mobile, token, insurance_centre_sub_domain, alias_name, resource, x_api_key)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |




[Back to List of Controllers](#list_of_controllers)

## <a name="third_party_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ThirdPartyInsuranceController") ThirdPartyInsuranceController

### Get controller instance

An instance of the ``` ThirdPartyInsuranceController ``` class can be accessed from the API Client.

```python
 third_party_insurance_controller = client.third_party_insurance
```

### <a name="get_car_brands"></a>![Method: ](https://apidocs.io/img/method.png ".ThirdPartyInsuranceController.get_car_brands") get_car_brands

> دریافت لیست برند خودرو ها

```python
def get_car_brands(self,
                       car_type_group,
                       x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| carTypeGroup |  ``` Required ```  | شناسه ی گروه خودرو |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
car_type_group = 1
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = third_party_insurance_controller.get_car_brands(car_type_group, x_api_key)

```


### <a name="get_risk_level"></a>![Method: ](https://apidocs.io/img/method.png ".ThirdPartyInsuranceController.get_risk_level") get_risk_level

> دریافت لیست تخفیف های بیمه

```python
def get_risk_level(self,
                       insurance_policy_type,
                       x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| insurancePolicyType |  ``` Required ```  | شناسه ی نوع بیمه نامه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
insurance_policy_type = 0
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = third_party_insurance_controller.get_risk_level(insurance_policy_type, x_api_key)

```


### <a name="get_car_brand_tips"></a>![Method: ](https://apidocs.io/img/method.png ".ThirdPartyInsuranceController.get_car_brand_tips") get_car_brand_tips

> دریافت لیست تیپ خودرو

```python
def get_car_brand_tips(self,
                           car_brand_id,
                           x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| carBrandId |  ``` Required ```  | شناسه ی برند خودرو |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
car_brand_id = 190
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = third_party_insurance_controller.get_car_brand_tips(car_brand_id, x_api_key)

```


### <a name="get_car_uses"></a>![Method: ](https://apidocs.io/img/method.png ".ThirdPartyInsuranceController.get_car_uses") get_car_uses

> دریافت لیست نوع کاربری خودرو

```python
def get_car_uses(self,
                     car_type_id,
                     x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| carTypeId |  ``` Required ```  | شناسه ی نوع خودرو |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
car_type_id = 103
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = third_party_insurance_controller.get_car_uses(car_type_id, x_api_key)

```


### <a name="get_has_plan"></a>![Method: ](https://apidocs.io/img/method.png ".ThirdPartyInsuranceController.get_has_plan") get_has_plan

> آیا این نوع بیمه نامه، طرح بیمه ای دارد؟

```python
def get_has_plan(self,
                     sub_domain,
                     insurance_policy_type,
                     x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insurancePolicyType |  ``` Required ```  | شناسه ی نوع بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_policy_type = 0
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = third_party_insurance_controller.get_has_plan(sub_domain, insurance_policy_type, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="motorcycle_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MotorcycleInsuranceController") MotorcycleInsuranceController

### Get controller instance

An instance of the ``` MotorcycleInsuranceController ``` class can be accessed from the API Client.

```python
 motorcycle_insurance_controller = client.motorcycle_insurance
```

### <a name="get_car_brands"></a>![Method: ](https://apidocs.io/img/method.png ".MotorcycleInsuranceController.get_car_brands") get_car_brands

> دریافت لیست برند موتور سیکلت

```python
def get_car_brands(self,
                       car_type_group,
                       x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| carTypeGroup |  ``` Required ```  | شناسه ی گروه خودرویی، موتور سیکلت =>0 |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
car_type_group = 0
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = motorcycle_insurance_controller.get_car_brands(car_type_group, x_api_key)

```


### <a name="get_car_brand_tips"></a>![Method: ](https://apidocs.io/img/method.png ".MotorcycleInsuranceController.get_car_brand_tips") get_car_brand_tips

> دریافت لیست تیپ موتور سیکلت

```python
def get_car_brand_tips(self,
                           car_brand_id,
                           x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| carBrandId |  ``` Required ```  | شناسه ی برند موتور سیکلت |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
car_brand_id = 472
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = motorcycle_insurance_controller.get_car_brand_tips(car_brand_id, x_api_key)

```


### <a name="get_has_plan"></a>![Method: ](https://apidocs.io/img/method.png ".MotorcycleInsuranceController.get_has_plan") get_has_plan

> آیا این نوع بیمه نامه، طرح بیمه ای دارد؟

```python
def get_has_plan(self,
                     sub_domain,
                     insurance_policy_type,
                     x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insurancePolicyType |  ``` Required ```  | شناسه ی نوع بیمه نامه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_policy_type = 7
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = motorcycle_insurance_controller.get_has_plan(sub_domain, insurance_policy_type, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="fire_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FireInsuranceController") FireInsuranceController

### Get controller instance

An instance of the ``` FireInsuranceController ``` class can be accessed from the API Client.

```python
 fire_insurance_controller = client.fire_insurance
```

### <a name="get_fire_insurance"></a>![Method: ](https://apidocs.io/img/method.png ".FireInsuranceController.get_fire_insurance") get_fire_insurance

> دریافت اطلاعات پایه بیمه ی آتش سوزی

```python
def get_fire_insurance(self,
                           sub_domain,
                           insurance_policy_id,
                           x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insurancePolicyId |  ``` Required ```  | شناسه ی بیمه نامه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_policy_id = 0
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = fire_insurance_controller.get_fire_insurance(sub_domain, insurance_policy_id, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="earthquake_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EarthquakeInsuranceController") EarthquakeInsuranceController

### Get controller instance

An instance of the ``` EarthquakeInsuranceController ``` class can be accessed from the API Client.

```python
 earthquake_insurance_controller = client.earthquake_insurance
```

### <a name="get_earthquake"></a>![Method: ](https://apidocs.io/img/method.png ".EarthquakeInsuranceController.get_earthquake") get_earthquake

> دریافت اطلاعات پایه ی بیمه ی زلزله

```python
def get_earthquake(self,
                       sub_domain,
                       insurance_policy_id,
                       insurance_policy_type,
                       x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insurancePolicyId |  ``` Required ```  | شناسه ی بیمه نامه |
| insurancePolicyType |  ``` Required ```  | شناسه ی نوع بیمه نامه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_policy_id = 0
insurance_policy_type = 6
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = earthquake_insurance_controller.get_earthquake(sub_domain, insurance_policy_id, insurance_policy_type, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="travel_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TravelInsuranceController") TravelInsuranceController

### Get controller instance

An instance of the ``` TravelInsuranceController ``` class can be accessed from the API Client.

```python
 travel_insurance_controller = client.travel_insurance
```

### <a name="get_travel_insurance"></a>![Method: ](https://apidocs.io/img/method.png ".TravelInsuranceController.get_travel_insurance") get_travel_insurance

> TODO: Add Description

```python
def get_travel_insurance(self,
                             sub_domain,
                             insurance_policy_id,
                             x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insurancePolicyId |  ``` Required ```  | شناسه ی بیمه نامه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_policy_id = 0
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = travel_insurance_controller.get_travel_insurance(sub_domain, insurance_policy_id, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="elevator_insurance_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ElevatorInsuranceController") ElevatorInsuranceController

### Get controller instance

An instance of the ``` ElevatorInsuranceController ``` class can be accessed from the API Client.

```python
 elevator_insurance_controller = client.elevator_insurance
```

### <a name="get_elevator_insurance"></a>![Method: ](https://apidocs.io/img/method.png ".ElevatorInsuranceController.get_elevator_insurance") get_elevator_insurance

> دریافت اطلاعات پایه ی بیمه نامه ی آسانسور

```python
def get_elevator_insurance(self,
                               sub_domain,
                               insurance_policy_id,
                               x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insurancePolicyId |  ``` Required ```  | شناسه ی بیمه نامه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_policy_id = 0
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = elevator_insurance_controller.get_elevator_insurance(sub_domain, insurance_policy_id, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="main_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MainController") MainController

### Get controller instance

An instance of the ``` MainController ``` class can be accessed from the API Client.

```python
 main_controller = client.main
```

### <a name="get_portal_landing_page"></a>![Method: ](https://apidocs.io/img/method.png ".MainController.get_portal_landing_page") get_portal_landing_page

> در یافت اطلاعات لندینگ مراکز بیمه

```python
def get_portal_landing_page(self,
                                id,
                                x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
id = 'hfz1'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = main_controller.get_portal_landing_page(id, x_api_key)

```


### <a name="get_insurance_centre_policy_types"></a>![Method: ](https://apidocs.io/img/method.png ".MainController.get_insurance_centre_policy_types") get_insurance_centre_policy_types

> دریافت لیست بیمه ی های ارائه شده توسط مرکز بیمه

```python
def get_insurance_centre_policy_types(self,
                                          sub_domain,
                                          x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = main_controller.get_insurance_centre_policy_types(sub_domain, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="combo_data_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ComboDataController") ComboDataController

### Get controller instance

An instance of the ``` ComboDataController ``` class can be accessed from the API Client.

```python
 combo_data_controller = client.combo_data
```

### <a name="get_damage_type"></a>![Method: ](https://apidocs.io/img/method.png ".ComboDataController.get_damage_type") get_damage_type

> دریافت لیست نوع خسارت

```python
def get_damage_type(self,
                        x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = combo_data_controller.get_damage_type(x_api_key)

```


### <a name="get_insurance_types"></a>![Method: ](https://apidocs.io/img/method.png ".ComboDataController.get_insurance_types") get_insurance_types

> دریافت لیست نوع بیمه نامه

```python
def get_insurance_types(self,
                            sub_domain,
                            issue_insurance,
                            x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| issueInsurance |  ``` Required ```  | دریافت بیمه نامه های قابل صدور |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
issue_insurance = False
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = combo_data_controller.get_insurance_types(sub_domain, issue_insurance, x_api_key)

```


### <a name="get_insurance_companies"></a>![Method: ](https://apidocs.io/img/method.png ".ComboDataController.get_insurance_companies") get_insurance_companies

> دریافت لیست شرکت های بیمه

```python
def get_insurance_companies(self,
                                sub_domain,
                                insurance_type_id,
                                x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| insuranceTypeId |  ``` Required ```  | شناسه ی نوع بیمه نامه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
insurance_type_id = 1
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = combo_data_controller.get_insurance_companies(sub_domain, insurance_type_id, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="tracking_damage_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TrackingDamageController") TrackingDamageController

### Get controller instance

An instance of the ``` TrackingDamageController ``` class can be accessed from the API Client.

```python
 tracking_damage_controller = client.tracking_damage
```

### <a name="get_tracking_code"></a>![Method: ](https://apidocs.io/img/method.png ".TrackingDamageController.get_tracking_code") get_tracking_code

> استعلام وضعیت خسارت

```python
def get_tracking_code(self,
                          tracking_code,
                          x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mTrackingCode |  ``` Required ```  | کد پیگیری خسارت |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
tracking_code = '/{TrackingCode}'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = tracking_damage_controller.get_tracking_code(tracking_code, x_api_key)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |




### <a name="create_tracking_damage"></a>![Method: ](https://apidocs.io/img/method.png ".TrackingDamageController.create_tracking_damage") create_tracking_damage

> ثبت خسارت بیمه

```python
def create_tracking_damage(self,
                               body,
                               x_api_key,
                               content_type)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | اطلاعات خسارت |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |
| contentType |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body_value = "{\r\n  \"personalityType\": 0,\r\n  \"trackingDamageStatus\": [\r\n    {\r\n      \"trackingDamageFile\": [\r\n        {\r\n          \"id\": 162747,\r\n          \"url\": \"https://media.easybimeh.com//Easybimeh/FileManager/InsuranceCentre/hfz1/637089119345134776.jpeg\",\r\n          \"title\": \"کارت شناسایی\"\r\n        }\r\n      ]\r\n    }\r\n  ],\r\n  \"description\": \"بدنه ی خودرو خسارت دیده\",\r\n  \"insuranceTypeId\": 1,\r\n  \"insuranceCompanyId\": 34,\r\n  \"insurancePolicyNumber\": \"123456\",\r\n  \"damageType\": \"مالی\",\r\n  \"name\": \"کاظم\",\r\n  \"nationalCode\": \"3080118383\",\r\n  \"mobile\": \"09018318086\",\r\n  \"insuredProfile\": \"پژو 405\",\r\n  \"subDomain\": \"hfz1\"\r\n}"
body = json.loads(body_value)
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'
content_type = 'application/json'

result = tracking_damage_controller.create_tracking_damage(body, x_api_key, content_type)

```


### <a name="get_status_status_collections"></a>![Method: ](https://apidocs.io/img/method.png ".TrackingDamageController.get_status_status_collections") get_status_status_collections

> دریافت لیست وضعیت های خسارت

```python
def get_status_status_collections(self,
                                      status_type,
                                      x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| statusType |  ``` Required ```  | نوع وضعیت ها ی خسارت => 0 |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
status_type = 0
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = tracking_damage_controller.get_status_status_collections(status_type, x_api_key)

```


### <a name="get_status"></a>![Method: ](https://apidocs.io/img/method.png ".TrackingDamageController.get_status") get_status

> دریافت اطلاعات وضعیت

```python
def get_status(self,
                   entity_id,
                   x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| entityId |  ``` Required ```  | شناسه ی وضعیت |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
entity_id = 1129
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = tracking_damage_controller.get_status(entity_id, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="footer_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FooterController") FooterController

### Get controller instance

An instance of the ``` FooterController ``` class can be accessed from the API Client.

```python
 footer_controller = client.footer
```

### <a name="get_portal_landing_contact_about"></a>![Method: ](https://apidocs.io/img/method.png ".FooterController.get_portal_landing_contact_about") get_portal_landing_contact_about

> دریافت اطلاعات درباره ی ما

```python
def get_portal_landing_contact_about(self,
                                         x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| xApiKey |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = footer_controller.get_portal_landing_contact_about(x_api_key)

```


### <a name="get_faq_insurance_centre"></a>![Method: ](https://apidocs.io/img/method.png ".FooterController.get_faq_insurance_centre") get_faq_insurance_centre

> دریافت لیست سوالات متداول

```python
def get_faq_insurance_centre(self,
                                 x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = footer_controller.get_faq_insurance_centre(x_api_key)

```


### <a name="get_insurance_policy_tracking"></a>![Method: ](https://apidocs.io/img/method.png ".FooterController.get_insurance_policy_tracking") get_insurance_policy_tracking

> پیگیری وضعیت بیمه نامه

```python
def get_insurance_policy_tracking(self,
                                      tracking_code,
                                      national_code,
                                      x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| trackingCode |  ``` Required ```  | شماره ی پیگیری بیمه نامه |
| nationalCode |  ``` Required ```  | کد ملی کاربر |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
tracking_code = 213981083
national_code = 3080115309
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = footer_controller.get_insurance_policy_tracking(tracking_code, national_code, x_api_key)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 500 | Internal Server Error |




[Back to List of Controllers](#list_of_controllers)

## <a name="insurance_policy_plan_controller"></a>![Class: ](https://apidocs.io/img/class.png ".InsurancePolicyPlanController") InsurancePolicyPlanController

### Get controller instance

An instance of the ``` InsurancePolicyPlanController ``` class can be accessed from the API Client.

```python
 insurance_policy_plan_controller = client.insurance_policy_plan
```

### <a name="get_special_plan"></a>![Method: ](https://apidocs.io/img/method.png ".InsurancePolicyPlanController.get_special_plan") get_special_plan

> دریافت لیست طرح های بیمه ای

```python
def get_special_plan(self,
                         sub_domain,
                         x_api_key)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| subDomain |  ``` Required ```  | دامنه یا زیر دامنه ی مرکز بیمه |
| xApiKey |  ``` Required ```  | کلید اختصاصی ارتباط با سرور |



#### Example Usage

```python
sub_domain = 'hfz1'
x_api_key = 'd6dfd932-75d8-e911-811a-000c294ecf01'

result = insurance_policy_plan_controller.get_special_plan(sub_domain, x_api_key)

```


[Back to List of Controllers](#list_of_controllers)



