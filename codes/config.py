import os
import socket
from codes.utils import sysModel
from pathlib import Path

# ------------------------------- control -------------------------------
# output the table, eg: kwh, fuel consumption, running hrs
REPORT_OUT_EXCEL = False

# ------------------------------- Auth -------------------------------
# ---------------- erp
ERP_HOST = "192.168.2.30"
ERP_PORT = 30015
ERP_USER = "APRREPORT"
# ERP_PW = "RrfFvUzrTjql7(@G"
SCHEMACHOICES = ['AP011_TRAINING2', 'AP011_UAT', 'AP000_UAT']

# ------------------------------- paths -------------------------------
# project_path
SER_PATH = sysModel.getTargetPath('220809_reportPythonServer')
PRJ_PATH = os.path.join(SER_PATH, 'reportProject')
PARENT_PATH = Path(SER_PATH).parent
paramPath = os.path.join(PRJ_PATH, 'codes')

# ------------------------------------------------------------------------------------------
hostname = socket.gethostname()
if (hostname == 'APDC-DATA02'):
    LOCATION = 'prod'  # dev / prod
else:
    LOCATION = 'dev'

# dev (Notebook environment)
if (LOCATION == 'dev'):
    monthlyReportDocsPath = os.path.join(PRJ_PATH, 'docs/monthlyReport')
    reportDataPath = os.path.join(monthlyReportDocsPath, "reportData")  # csv path
    sqliteOutPath = os.path.join(monthlyReportDocsPath, "sqliteData")  # sqlite path
    inoutRecordPath = os.path.join(monthlyReportDocsPath, "inOutRecord")
    logsPath = os.path.join(monthlyReportDocsPath, "logs")
    reportPath = os.path.join(monthlyReportDocsPath, "reports")
    pdfImagesPath = os.path.join(monthlyReportDocsPath, "pdfImages")
    tankSizePath = os.path.join(monthlyReportDocsPath, "tankSize")
    registeredPath = os.path.join(monthlyReportDocsPath, 'registerPlant')
    installedSSMEPath = os.path.join(monthlyReportDocsPath, 'installedSSME')
    tempPath = os.path.join(monthlyReportDocsPath, "pdfImages/temp")  # for storing the plot graph
    tempComparePlotsPath = os.path.join(
        "C:/Users/chris.cheung.APRENTALSHK/Desktop/Chris/projects/220219_APWebServer/dev-data/compareReport/plots")  # for storing the compare plot graph
    # terex report (move from generated dir to shared dir)
    terexReportFolder = os.path.join(monthlyReportDocsPath, "terexReport/reportFolder")
    terexReoirtSharedFolder = os.path.join(monthlyReportDocsPath, "terexReport/sharedFolder")
    nodeJsServerUrl = 'http://localhost:3001'
    # HK key project path
    keyProjectPath = 'C:/Users/chris.cheung.APRENTALSHK/Desktop/Chris/projects/211207_APrental/AP_creditFacility/docs/01. Request'
    # erp report directory
    erpDir = f'C:/Users/chris.cheung/Documents/AP_sapReportAlert/'
    # write unit files path
    unitFilePath = "C:/Users/chris.cheung/Desktop/Chris/projects/220219_APWebServer/dev-data/UnitFiles"

# prod (apdc-data02 environment)
elif (LOCATION == 'prod'):
    # prod (In server)
    monthlyReportDocsPath = os.path.join(PRJ_PATH, 'docs/monthlyReport')
    reportDataPath = "\\\\apdc-data01\\ComApAPIData"  # csv path
    sqliteOutPath = os.path.join("D:\\SSME Reports\\v2", "sqliteData")  # sqlite path
    inoutRecordPath = "\\\\apdc-data01\\UserData\\BA"
    logsPath = os.path.join(monthlyReportDocsPath, "logs")
    reportPath = "\\\\apdc-data02\\SSME Reports\\v2"
    pdfImagesPath = os.path.join(monthlyReportDocsPath, "pdfImages")
    tankSizePath = "C:\\SSME_Python\\Data"
    registeredPath = '\\\\apdc-data01\\ComApAPIData\\Units'
    installedSSMEPath = '\\\\apdc-dc01\\ShareData\\Data\\Inventory\\Machine\\Plant Master'
    tempPath = os.path.join(monthlyReportDocsPath, "pdfImages/temp")  # for storing the plot graph
    tempComparePlotsPath = os.path.join(
        "C:/Users/itsupport/projects/220219_APWebServer/dev-data/compareReport/plots")  # for storing the compare plot graph
    # terex report (move from generated dir to shared dir)
    terexReportFolder = "C:\\Terex_Python\\Reports"
    terexReoirtSharedFolder = "\\\\apdc-dc01\\ShareData\\Data\\WS-TA\\07.Tunneling\\Operator\\Terex   TA400\\ISM Reports"
    nodeJsServerUrl = 'http://localhost:3001'
    # HK key project path
    keyProjectPath = '\\\\apdc-data01\\UserData\\MP'
    # erp report directory
    erpDir = f'C:/Users/itsupport/Documents/AP_sapReportAlert/'
    # write unit files path
    unitFilePath = "D:\\WebSupervisorData\\UnitFiles"

colNameTable = {
    'float': {
        "Fuel Level": "fuel_level",
        "Fuel level": "fuel_level",  # that is noisy fuel level, need to filter out the zero fuel-level
        "Nomin power": "nominal_power",
        "Nominal Power": "nominal_power",
        "actual_power": "actual_power",
        "Act power": "actual_power",
        "Load kW": "actual_power",
        "Load P": "actual_power",
        "Generator P": "actual_power",
        "Generator kW": "actual_power",
        "Actual Power": "actual_power",
        "Genset kWh": "kwh",
        "kWh (Import)": "kwh",
        "RPM": "rpm",
        "Genset kVArh": "kvarh",
        "kVArhours": "kvarh",
        "Running Hours": "run_hours",
        "Run hours": "run_hours",
        "Run Hours": "run_hours",
        "Total Fuel Consumption": "fuel_cons",
        "Total / Trip Fuel Consumpt": "fuel_cons",
        "Fuel Rate": "fuel_rate",           # If Fuel Rate exist, then ECU. Otherwise, it is not ECU.
        "FuelRate": "fuel_rate",
        # "BatteryVoltage" : "battery_v",
        # "CoolantTemp" : "coolant_temp",
        # "Oil Press" : "oil_pressure",
        # "Engine Speed (RPM)" : "engine_rpm",
        # "Nominal RPM" : "nominal_rpm",
        # "Water temp" : "water_temp",
        # "Coolant Temp" : "water_temp",
    },
    'simple_string': {
        "ID String": "id_string",
    },
    # this is very time consume, as it fill all the value interval
    'interval_string': {
        "Communication State": "communication_state",
    }
}

inout_colNameTable = {
    "Signed DN/CR": "signed_dncr",
    "AC CODE": "flex_code",
    "租/售合同號碼": "contract_no",
    "工作/機械編號": "plant_no",
    "型號 ": "model",
    "機身編號": "machine_no",
    "出機時數 ": "out_meter_hr",
    "收機時數": "in_meter_hr",
    "收/送貨單編號": "in_out_dn_no",
    "出-1 /入 1": "in_out",
    "日": "day",
    "月": "month",
    "起/截租日": "billing_date",
    "客戶名稱 ": "customer_name",
    "Rental Rate/ Sales Price": "rental_sales_price",
    "運輸公司名稱": "transp_com_name",
    "車牌號碼 ": "plate_no",
    "取機位置 ": "collect_loc",
    "送/收機位置 ": "in_out_loc",
    "實際用機位置": "act_usage_loc",
    "運輸成本": "transp_cost",
    "附加費用": "extra_charge",
    "客戶支付": "customer_paid",
    "賬號": "ledger",
    "損壞索償": "demage_claim",
    "Salesman Code": "salesmancode",
    "New Customer": "new_cust",
    "MAR": "mar",
    "Last/First Invoice ": "last_first_invoice",
    "MACHINE OT Hour": "machine_ot_hr",
    "MACHINE OT Hour ": "machine_ot_hr",
    "MACHINE OT Invoice": "machine_ot_inv",
    "PLANT SHEET": "plant_sheet",
    "Plant Sheet": "plant_sheet",
    "Recevied from 8A": "recevied_8a",
    "備註": "remark1",
    "Inspection Form Rec'd ": "insp_rec",
    "Claim ": "claim",
    "Claim waived ": "claim_waived",
    "Diesel ": "diesel",
    "Diesel": "diesel",
    "Remarks ": "remark2",
    "年": "year"
}

# for replace the item master column into database col name
plantMasterColName = {
    "Plant No": "plantno",
    "Status": "status",
    "Product Class": "productClass",
    "Product Category": "productCategory",
    "Brand": "brand",
    "Model": "model",
    "Fuel Tank Capacity (L)": "fuelTankCapacity",
    "SSME Bundle no.": "ssmeBundle",
}

# for replace the machine master column into database col name
plantMasterColName_sap = {
    "Code": "plantno",
    "Existence": "status",
    "U_ProductClass": "productClass",
    "U_ProductCat": "productCategory",
    "U_Brand": "brand",
    "U_ModelPartsCode": "model",
    "fuelTankCap": "fuelTankCapacity", # need to refactor the columns before using this column
    "U_SmaNo": "ssmeBundle",
}

keyProjectColName = {
    "Key Project": "keyProject",
    " Project Code": "projectCode",
    "Contract No.": "contractNo",
    "Contract Title": "contractTitle",
    "Main Contractor": "mainContractor",
    "Responsible Salesman": "responsibleSalesman",
    "Contract Award Date": "contractAwardDate",
    "Estimated End Date": "estimatedEndDate",
    "Contract Amount (MHKD)": "contractAmount",
    "Update on": "updateOn",
    "link for reference": "link"
}

# webserver login
WEB_LOGINNAME = 'ap_superuser'
WEB_PASSWORD = 'NZrq74MzVCwPwbqiBE33'

# ------------------------------- html -----------------------------------
DEFAULT_HTML = """
<h2>Testing</h2>
"""

DAILY_SUMMARY_HTML = """
                    <style>
                      * {
                        box-sizing: border-box;
                      }
                      table,
                      td {
                        border: 1px solid black;
                        text-align: center;
                      }
                      .header-row {
                        height: 30px;
                      }
                      /* table {
                        width: 1000px;
                      } */
                      .table-container {
                        margin: 30px;
                      }
                      .header {
                        font-weight: 700;
                        font-size: 18px;
                      }
                      .black {
                        background-color: black;
                      }
                      .red {
                        background-color: rgb(255, 94, 0);
                        color: white;
                      }
                      .yellow {
                        background-color: rgb(255, 230, 0);
                      }
                      .green {
                        background-color: rgb(0, 255, 34);
                        color: white;
                      }
                      .grey {
                        background-color: rgb(102, 102, 102);
                        color: white;
                      }
                      .small-width {
                        width: 100px;
                      }
                      .meddle-width {
                        width: 200px;
                      }
                      .wide-width {
                        width: 400px;
                      }
                    </style>
                    <body>
                      <h2>SSME Daily Report</h2>
                      <div class="table-container">
                        <table>
                          <tr class="header-row">
                            <td class="small-width"></td>
                            <td class="small-width header">Data</td>
                            <td class="wide-width" colspan="2">Yes</td>
                            <td class="wide-width" colspan="2">No</td>
                          </tr>
                          <tr class="header-row">
                            <td></td>
                            <td class="header">IN/OUT</td>
                            <td class="middle-width">Yes</td>
                            <td class="middle-width">No</td>
                            <td class="middle-width">Yes</td>
                            <td class="middle-width">No</td>
                          </tr>
                          <tr>
                            <td class="header">Registered</td>
                            <td class="header">Installed</td>
                            <td class="black"></td>
                            <td class="black"></td>
                            <td class="black"></td>
                            <td class="black"></td>
                          </tr>
                          <tr>
                            <td rowspan="2">Yes</td>
                            <td>Yes</td>
                            <td class="green">(1,1,1,1)</td>
                            <td>(1,1,1,0)</td>
                            <td class="red">(1,1,0,1)</td>
                            <td>(1,1,0,0)</td>
                          </tr>
                          <tr>
                            <td>No</td>
                            <td class="yellow">(1,0,1,1)</td>
                            <td class="yellow">(1,0,1,0)</td>
                            <td class="yellow">(1,0,0,1)</td>
                            <td class="yellow">(1,0,0,0)</td>
                          </tr>
                          <tr>
                            <td rowspan="2">No</td>
                            <td>Yes</td>
                            <td class="yellow">(0,1,1,1)</td>
                            <td class="yellow">(0,1,1,0)</td>
                            <td class="yellow">(0,1,0,1)</td>
                            <td class="yellow">(0,1,0,0)</td>
                          </tr>
                          <tr>
                            <td>No</td>
                            <td class="red">(0,0,1,1)</td>
                            <td class="red">(0,0,1,0)</td>
                            <td>(0,0,0,1)</td>
                            <td>(0,0,0,0)</td>
                          </tr>
                        </table>
                      </div>
                    </body>
"""

MONTHLY_REPORT_NOTICE_HTML = """
<div>
  <p>Dear Sir/Madam,</p>
  <p style="padding-left: 20px">The report is out.</p>
  <p style="padding-left: 20px">
    Please check
    <a href="{}">HERE</a>
  </p>
</div>
"""

TEREX_REPORT_MOVEMENT_NOTICE_HTML = """
<div>
  <p>Dear Sir/Madam,</p>
  <p style="padding-left: 20px">The Terex files is moved on this path:</p>
  <p style="padding-left: 40px">{}</p>
</div>
"""

FOOTER_HTML = """

"""
