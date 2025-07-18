<h1>LapoMfb Loan and Savings Calculator</h1>

 ### [DASHBOARD LINK](https://app.powerbi.com/groups/me/reports/3be2a217-62eb-4ac7-80b9-9b44f5536b06/d6b7fa55e4c18dcfc3d5?experience=power-bi)

<h2>Description</h2>
This dashboard gives a clear, interactive view of how customers are transacting across different zones, branches, and account products. It’s designed to help teams understand where money is moving, which platforms are being used, and which products are driving activity.It was developed to enable operations, product, and customer service teams to
Monitor overall transaction volume,
Identify top-performing digital channels,
Track usage trends by zone and branch,
Drill down to individual customer behavior for better service targeting.
With over ₦1 billion in transaction value, this dashboard reveals which channels and account types are driving the most activity and revenue.


<br />


<h2>📂 Tools & TechnologiesUsed</h2>

- <b>SQL	Data extraction, transformations</b> 
- <b>Power BI	Data visualization & reporting</b>


<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

<h2>Steps Followed:</h2>

<p align="center">
Step 1: Data Preparation 
<img src="https://i.imgur.com/vs1hLq0.jpeg" height="80%" width="80%" alt="Channels dashboard"/>

<p align="left">SQL queries were used to extract transaction records from core banking systems.
<br>Important fields included: USER_ID, ACCOUNT_NAME, TRN_DESC, AMOUNT, ZONE, BRANCH_NAME, CUSTOMER_NAME.</br>

<br />
<br />
<p align="center">
Step 2: Power BI load <br/>
<img src="https://i.imgur.com/OsNL3Se.jpeg" height="80%" width="80%" alt="Power Query Steps Steps"/>
 
 <p align="left">Data loaded directly from CSV extracts into Power BI Desktop.
  
  <br>Relationships automatically detected and adjusted as necessary.
  Light transformation was done (most data was already clean).

Verified column data types and filtered out non-essential transactions (REV%, SDC, VAT, etc.).

Ensured no sensitive fields (e.g. mobile numbers) were retained in the report.

</br>
</br>
<p align="center">
Step 3: Visual Design <br/>
<img src="https://i.imgur.com/CAhtiTQ.jpeg" height="80%" width="80%" alt="Dashbaord Design"/>
 
 <p align="left">A Decomposition Tree Visual was used to break down transaction flow in this order:
  
  <br>Platform ➝ Account Product ➝ Transaction Type ➝ Zone ➝ Branch ➝ Customer Name

Verified column data types and filtered out non-essential transactions (REV%, SDC, VAT, etc.).

📈 Insights
Total Transaction Volume: ₦1,073,043,066.09

Top Channels by Volume:

FLEXSWITCH: ₦948M+

LAPOIBANKMOB: ₦113M+

NIPINCM: ₦6.6M

Most Used Products:

Savings Account - Staff

Regular Savings

Xpress Savings

Top Zones by Activity:

Lagos Mainland Zone

FCT Zone

Lagos West Zone


<br />
<br />


 
<br />
<br />


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
