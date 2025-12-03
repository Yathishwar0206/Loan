import streamlit as st
import numpy as np
import joblib

st.sidebar.image(log.jpg,width=150)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to",["Home","About","Types","Rules and Regulations for Customers","Prediction","Contact"])
st.sidebar.write("Your satisfaction is our service.")

# Home page

if page == "Home":
   page_bg = """
   <style>
   [data-testid="stAppViewContainer"] {
   background-image: url("https://static.vecteezy.com/system/resources/previews/023/221/109/non_2x/banking-and-finance-concept-digital-connect-system-financial-and-banking-technology-with-integrated-circles-glowing-line-icons-and-on-blue-background-design-vector.jpg");
   background-size: cover;
   }
   </style>
   """
   st.markdown(page_bg, unsafe_allow_html=True)
   st.markdown("<h1 style='text-align:center;'>YR bank pvt.ltd</h1>", unsafe_allow_html=True)
   st.caption("<h2 style='text-align:center;'> Your satisfaction is our service </h2>",unsafe_allow_html=True)
   st.logo(log.jpg)
   st.set_page_config(layout='centered')
   col1, col2, col3 = st.columns([1,1,1.05])
   with col2:
       st.logo("log.jpg")
       st.image("log.jpg",width=200)
 
# About us

elif page == "About":
  page_bg = """
   <style>
   [data-testid="stAppViewContainer"] {
   background-image: url("https://static.vecteezy.com/system/resources/previews/023/221/109/non_2x/banking-and-finance-concept-digital-connect-system-financial-and-banking-technology-with-integrated-circles-glowing-line-icons-and-on-blue-background-design-vector.jpg");
   background-size: cover;
   }
   </style>
   """
  st.markdown(page_bg, unsafe_allow_html=True)
  st.title("About us")
  st.write("""
Welcome to Our website!
This page give information about our service.
""")
  st.header("🏦 YR bank pvt.ltd")
  st.write("""
We are give the service for the customers who are they want a Financial help.
According to your proper evidence and proofs, we providing loan for your needs and
you can get sufficient loan.""")
  st.write("We are make customer to Satisfy their needs.")
  
  st.header("🎯 Our Mission")
  st.write("""
Our mission is to make  customer satisfy and become one of the trusted financial institution
for the customer.        
""")
  
  st.header("What we Do")
  st.write("""
- Satisfy customer needs
- Build trust
- Giving loans
- Providing gold loans
- Having Safety locker for your securities.
         """)
  
  st.header("Branches")
  st.write("""
1. Chennai
2. Madurai
3. Tirunelveli
4. Nagercoil
5. Coimbatore
6. Tanjore
7. Thiruchirappalli
8. Trivandrum
9. Kochi
10.Bangalore.""")

# Rules and Regulation
elif page == "Rules and Regulations for Customers":
       page_bg = """
   <style>
   [data-testid="stAppViewContainer"] {
   background-image: url("https://static.vecteezy.com/system/resources/previews/023/221/109/non_2x/banking-and-finance-concept-digital-connect-system-financial-and-banking-technology-with-integrated-circles-glowing-line-icons-and-on-blue-background-design-vector.jpg");
   background-size: cover;
   }
   </style>
   """
       st.markdown(page_bg, unsafe_allow_html=True)
       st.title("Rules and Regulations for Customers")
       st.header('Top 10 Rules and Regulations for Customer')
       st.write("""
1.Keep your account information private – Don’t share your PIN, password, or OTP with anyone.

2.Maintain minimum balance – Keep the required minimum balance to avoid penalties.

3.Update personal details – Inform the bank if your phone number, address, or email changes.

4.Check your statements regularly – Make sure all transactions are correct.

5.Use ATM safely – Cover the keypad while entering your PIN.

6.Report lost cards immediately – Inform the bank at once if your card or phone is lost.

7.Do not sign blank forms – Always fill all details before signing any bank document.

8.Follow YR bank pvt.ltd rules – Submit valid ID and address proof when required.

9.Avoid sharing bank details over calls/messages – Banks never ask for sensitive information.

10.Respect transaction limits – Follow daily withdrawal and transfer limits set by the bank.
                """)


# Types of Loans

elif page == "Types":
    page_bg = """
   <style>
   [data-testid="stAppViewContainer"] {
   background-image: url("https://static.vecteezy.com/system/resources/previews/023/221/109/non_2x/banking-and-finance-concept-digital-connect-system-financial-and-banking-technology-with-integrated-circles-glowing-line-icons-and-on-blue-background-design-vector.jpg");
   background-size: cover;
   }
   </style>
   """
    st.markdown(page_bg, unsafe_allow_html=True)
    st.title("Types of Loans")
    
    st.header("Personal Loans")
    st.image("personal.jpg",width=800)
    st.write("""
             A personal loan is an unsecured loan that provides a lump sum of money for various personal uses, such as weddings, medical expenses, home renovations, or debt consolidation. It does not require you to provide any collateral, such as a house or car. 
            Key Features and Benefits
             Flexible Usage: The funds can be used for almost any legitimate personal purpose, unlike specific-purpose loans (like a home or education loan).
             Unsecured: No collateral or guarantor is needed to obtain the loan, with approval based on your creditworthiness and income.
             Fixed Repayment: The loan is repaid through fixed monthly installments (EMIs) over a pre-determined tenure, typically ranging from 12 to 60 months (though some lenders offer up to 84 months).
             Quick Processing: Many lenders offer a fully digital application process with minimal documentation, allowing for quick approval and disbursal of funds, often within hours or a few days.
             Predictable EMIs: With a fixed interest rate, your monthly payments remain consistent throughout the loan term, making budgeting easier. 
             Eligibility Criteria
             Eligibility generally depends on your financial profile, and criteria may vary among lenders. Common requirements include: 
             Age: Typically between 21 and 60 years old.
             Nationality: Must be an Indian citizen or resident.
             Income: A stable monthly income is essential (e.g., minimum ₹25,000 per month, though this can vary by city and lender).
             Credit Score: A good credit score (typically 720 or above) increases your chances of approval and helps secure a better interest rate.
             Employment Stability: A stable job history, often with a minimum of 1-2 years of work experience, is preferred by lenders. 
             
             
             How to Apply : 
             The application process is typically straightforward: 
             Check Eligibility: Use an online personal loan eligibility calculator to estimate the amount you may qualify for.
             Compare Offers: Review interest rates and terms from various banks and financial institutions to find the best fit for your needs on platforms like Paisabazaar or the lender's direct website/app.
             Submit Application: Fill out the application form with personal and financial details.
             Upload Documents: Provide necessary documents, such as identity proof (Aadhaar, PAN Card), address proof, and income proof (salary slips, bank statements, ITR forms).
             Receive Funds: Once approved, the loan amount is quickly disbursed to your bank account
             """)
    
    st.header("Vehicle Loans")
    st.image("vehical.jpg",width=800)
    st.write("""
             A vehicle loan, also known as an auto loan, is a type of secured installment loan used to finance the purchase of a new or used vehicle. The vehicle itself serves as collateral, which means the lender can repossess it if the borrower fails to make payments. 
             How Vehicle Loans Work
             Principal and Interest: The lender provides funds to cover most or all of the vehicle's price. This borrowed amount (principal) is repaid over a set period (tenure) through fixed monthly installments (EMIs), which include both principal and interest.
             Down Payment: While some lenders offer 100% financing, a down payment is often required, which reduces the loan amount and can lead to better interest rates.
             Loan Term (Tenure): Repayment periods are flexible, typically ranging from 12 months to 84 months (1 to 7 years), with longer tenures resulting in lower monthly payments but potentially higher overall interest costs.
             InterestRates: Rates are determined by the borrower's creditworthiness (a credit score above 720-750 is ideal for the best rates), the loan term, and current market conditions.
             Hypothecation: The vehicle is typically hypothecated (financially linked) to the lender until the loan is fully repaid. Once the loan is closed, the hypothecation can be removed from the vehicle's registration certificate. 
             
             Types of Vehicle Loans :
             New Car Loan: For purchasing a brand-new vehicle, often with financing options up to 100% of the on-road price.
             Used Car Loan: For financing a pre-owned vehicle, usually offering financing of 75-85% of the car's value for a shorter tenure than new car loans.
             Two-Wheeler Loan: Specifically for motorcycles, scooters, or mopeds, with terms and loan amounts tailored for these vehicles.
             Green Car Loan: A specialized loan for purchasing electric vehicles (EVs), which may offer concessional interest rates and up to 100% funding as an incentive.
             Loan Against Car: Allows an existing car owner to use their vehicle as collateral for a separate loan, often providing quick access to funds. 
             
             General Eligibility Criteria :
             Criteria vary by lender, but common requirements include: 
             Age: Typically between 18 or 21 and 60 or 65 years old at the time of loan maturity.
             Income: A stable source of income with a specified minimum monthly or annual income (e.g., around ₹25,000 per month for salaried individuals in some cases).
             redit Score: A good credit score is important for quick approval and favorable terms.
             Employment: Minimum one to two years of stable employment or business history. 
             
             Application Process :
             The application process can often be completed online and generally requires minimal documentation. 
             Compare Offers: Research and compare interest rates and terms from different lenders (banks, dealerships, financial institutions).
             Submit Application: Fill out the application form with personal and employment details.
             Provide Documents: Submit required documents such as proof of identity (Aadhaar, PAN card, passport), address, and income (salary slips, ITR, bank statements).
             Verification and Approval: The lender verifies the information and credit profile to approve the loan.
             Disbursal: Upon approval, the funds are disbursed directly to the vehicle dealer. 
             """)
    
    st.header("Education Loans")
    st.image("education.png",width=800)
    st.write("""
             An education loan is a sum of money borrowed to finance higher education and related expenses such as tuition, books, living costs, and travel. In India, students can access loans through government schemes (like PM-Vidyalaxmi) and private lenders, with varying interest rates, loan limits, and repayment terms. 
             
             Key Features
             Covera  Loans generally cover most education-related expenses, including admission fees, tuition, examination/library/laboratory fees, purchase of study materials/computers, and caution deposits.
             Moratorium Period: Most loans offer a repayment-free period (moratorium) covering the course duration plus one year, or six months after securing a job, whichever is earlier.
             Collateral: For loans up to ₹7.5 lakhs, collateral or a third-party guarantee is typically not required under government schemes. Higher loan amounts may require tangible collateral security.
             Interest Rates: Interest rates vary by lender and scheme. Government schemes often have lower, subsidized interest rates for eligible students, with potential concessions for female students.
             Repayment: The repayment period can extend up to 15 years after the moratorium period, with no pre-payment penalties in most cases.
             Tax Benefits: Interest paid on education loans is eligible for tax deductions under Section 80E of the Income Tax Act, 1961. 
             Government Schemes in India.
             
             The government offers several schemes to make education loans accessible, primarily through the unified PM-Vidyalaxmi portal. 
             PM-Vidyalaxmi Scheme: A platform to apply for education loans and interest subvention schemes. It facilitates a simple, transparent, and entirely digital application process.
             Central Sector Interest Subsidy (CSIS) Scheme: Provides full interest subsidy during the moratorium period for students from Economically Weaker Sections (EWS) with an annual family income up to ₹4.5 lakhs, for professional/technical courses in India.
             Credit Guarantee Fund Scheme for Education Loans (CGFSEL): Under this scheme, the central government provides a guarantee for loans up to ₹7.5 lakhs availed without collateral. 
             General Eligibility Criteria.
             
             While criteria vary among lenders, general requirements include: 
             Indian citizenship.
             Confirmed admission to a recognized institution or university.
             Age typically between 16 and 35 years.
             A co-applicant (parent/guardian/blood relative) with a stable income and creditworthiness. 
             
             Application Process : 
             The application process can be completed online via the government portal or individual bank websites. It typically involves: 
             Checking eligibility and gathering necessary documents (academic records, admission letter, ID proof, income proof of co-applicant).
             Filling out the application form.
             Verification of documents and details by the lender.
             Sanction and direct disbursement of the loan amount to the institution. 
             """)
    st.header("Medical Loans")
    st.image("medical.jpg",width=800)
    st.write("""
             A medical loan is a type of personal loan used to cover healthcare expenses, whether for an unexpected medical emergency or a planned treatment. These are typically unsecured loans, meaning they do not require collateral, and are offered by various financial institutions. 
             
             Key Features and Uses
             Coverage: Funds can cover a wide range of costs not fully covered by health insurance, including deductibles, co-payments, hospital bills, surgeries, diagnostic tests, and prescription medicines.
             Unsecured: Most medical loans are unsecured personal loans, relying on the borrower's creditworthiness rather than assets.
             Quick Disbursal: Lenders often provide quick approval and disbursal, which is crucial during medical emergencies.
             Flexible Repayment: These loans typically feature flexible repayment tenures and competitive interest rates.
             
             Eligibility: Eligibility criteria often include age limits, employment status, minimum income, and a strong credit score (e.g., a CIBIL score of 750 or above in India). 
             
             How to Apply :
             The application process is usually quick and can often be completed online: 
             Online Application: Fill out basic personal and financial details on a lender's website or app.
             Document Submission: Provide required documents, which generally include:
             KYC documents: Aadhaar card, PAN card, etc.
             Financial documents: Bank statements (e.g., last 6 months), income proof
             Verification and Approval: The lender verifies the application and documents.
             Fund Disbursal: Once approved, the loan amount is quickly transferred to the bank account. 
             For specific application details and requirements, you can check with various providers such as Poonawalla Fincorp, Tata Capital, or Paisabazaar. 
             their Related Loans
             Medical Equipment Loans: Specifically for healthcare providers (doctors, clinics, hospitals) to purchase or lease medical equipment like diagnostic or surgical tools.
             Doctor Loans: Specialized financial products for medical professionals to cover expenses such as clinic upgrades, renovations, or expansion. 
             """)
    
    st.header("Agricultural Loans")
    st.image("agri-loans.png",width=800)
    st.write("""
             Agriculture loans are financial programs that provide accessible and affordable credit to farmers for a wide range of farming and allied activities. These loans, offered by banks and government institutions (often with subsidies), support essential expenses like purchasing seeds, equipment, and livestock, and funding land development or infrastructure. 
             
             Key Types of Agriculture Loans
             Agriculture loans are categorized based on their purpose and repayment tenure: 
             Loan Type 	Purpose	Tenure
             Crop Loans	To cover short-term expenses for cultivation, including seeds, fertilizers, pesticides, and labor.	Short-term (tied to harvest period)
             Farm Mechanization	To purchase modern machinery like tractors, harvesters, and irrigation systems to enhance efficiency.	Medium/Long-term
             Allied Activities	For related sectors such as dairy, poultry, fisheries, and animal husbandry.	Variable
             Land Development	To fund improvements to the quality of land, construct irrigation channels, or purchase agricultural land.	Long-term (up to 15 years)
             Storage & Marketing	To build storage facilities or transport produce to avoid distress sales and fetch better market prices.	Variable
             
             Popular Schemes
             Kisan Credit Card (KCC) Scheme: A government-backed initiative that provides farmers with a single-window, hassle-free credit facility to meet their short-term requirements and a long-term loan component for investment credit. It often includes interest subvention for timely repayment.
             Agriculture Infrastructure Fund (AIF): A scheme offering low-interest loans for post-harvest management infrastructure, such as cold storage and warehouses.
             Pradhan Mantri Kisan Samman Nidhi (PM-KISAN): This scheme provides direct income support of ₹6,000 per year to eligible farmer families, not a loan, to help with general expenses. 
             
             Eligibility & Documentation
             General eligibility criteria include:
             Being an individual farmer, tenant farmer, sharecropper, or part of a Self-Help Group (SHG) or Joint Liability Group (JLG).
             Age between 18 and 70 years.
             Having ownership or lease access to agricultural land. 
             
             Required documents typically include:
             A duly filled application form.
             Identity and address proof (Aadhaar Card, Voter ID, etc.).
             Land ownership or lease documents, certified by revenue authorities.
             Income proof or bank statements. 
             """)
    
    st.header("Gold Loans")
    st.image("gold.webp",width=800)
    st.write("""
             A gold loan is a secured loan that allows a borrower to obtain funds by pledging gold ornaments or jewellery as collateral. This type of loan is popular for its quick processing, minimal documentation requirements, and lower interest rates compared to unsecured personal loans, as the gold itself acts as security. 
             
             Key Features
             Secured Nature: The loan is secured by your gold assets, which are stored securely by the lender until the loan is fully repaid.
             Quick Disbursal: Funds are typically disbursed quickly, often on the same day, due to the minimal documentation and collateral-based approval process.
             No CreditCheck Required: Since the loan is secured by an asset, a strong credit score or proof of income is often not a primary requirement for approval, making it accessible to a wide range of individuals.
             Flexible End-Use: The funds can be used for various purposes, such as medical emergencies, education expenses, business needs, or weddings, without end-use monitoring (except for capital market use or purchasing jewellery in some cases).
             Loan-to-Value (LTV) Ratio: Lenders typically offer a loan amount of up to 75% of the current market value of the gold, as per Reserve Bank of India (RBI) guidelines.
             Repayment Options: Options usually include regular monthly installments (EMI), paying only the interest during the tenure and the principal at the end (bullet repayment), or a combination of both. 
             
             Eligibility and Documentation
             
             Eligibility criteria are generally simple: 
             You must be an Indian resident, typically between 18 and 75 years of age.
             You must be the owner of the gold being pledged.
             The gold pledged is usually in the form of ornaments or jewellery with a purity between 18-karat and 22-karat. Gold coins (up to 50 grams per customer at some banks like SBI) may also be accepted, but not generally gold bars or biscuits. 
             Required documents typically include:
             Identity proof (e.g., Aadhaar Card, PAN Card, Voter ID, Passport, Driver's License).
             Address proof (e.g., Passport, Driver's License, electricity/utility bill).
             Passport size photographs. 
             
             Considerations and Risks
             Default Consequences: Failure to repay the loan can lead to penal charges and, as a last resort, the lender may auction the gold to recover the outstanding dues after a stipulated period and formal notices.
             Interest Rates and Fees: While interest rates are generally lower than unsecured loans, they can vary between lenders (banks and NBFCs) and schemes, so comparing rates and associated charges (processing fees, foreclosure charges, etc.) is important.
             Market Fluctuations: The loan amount is tied to the market value of gold. If gold prices drop significantly, the lender may ask for part repayment or additional collateral to maintain the LTV ratio.
            """)
  
# Prediction

elif page == "Prediction":
    page_bg = """
   <style>
   [data-testid="stAppViewContainer"] {
   background-image: url("https://static.vecteezy.com/system/resources/previews/023/221/109/non_2x/banking-and-finance-concept-digital-connect-system-financial-and-banking-technology-with-integrated-circles-glowing-line-icons-and-on-blue-background-design-vector.jpg");
   background-size: cover;
   }
   </style>
   """
    st.markdown(page_bg, unsafe_allow_html=True)
    st.title("🏦 Loan Approval Prediction App")
    
    # Load model and scaler
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("rf_model.pkl")

    # Input fields

    self_employed = st.selectbox("Self Employed",[0,1])
    income_annum = st.number_input("Income per year", min_value=0, value=1000000)
    loan_amount = st.number_input("Loan Amount", min_value=0, value=500000)
    loan_term = st.number_input("Loan Term (months)", min_value=0, value=36)
    cibil_score = st.number_input("CIBIL Score", min_value=0, value=750)
    total_asset_value = st.number_input("Total Asset Value", min_value=0, value=1000000)

     # Input array

    if st.button("🔍 Predict Loan Status"):
        input_data = np.array([[
            self_employed,
            income_annum,
            loan_amount,
            loan_term,
            cibil_score,
            total_asset_value
            ]])
        
         # Scale
        input_scaled = scaler.transform(input_data)
        
        
        prediction = model.predict(input_scaled)[0]
        # Predict
        if prediction == 1:
            st.success("✅ Loan Approved!")
        else:
            st.error("❌ Loan Rejected")

elif page == "Contact":
    page_bg = """
   <style>
   [data-testid="stAppViewContainer"] {
   background-image: url("https://static.vecteezy.com/system/resources/previews/023/221/109/non_2x/banking-and-finance-concept-digital-connect-system-financial-and-banking-technology-with-integrated-circles-glowing-line-icons-and-on-blue-background-design-vector.jpg");
   background-size: cover;
   }
   </style>
   """
    st.markdown(page_bg, unsafe_allow_html=True)
    st.title("📞 Contact us")
    st.write("Feel free to reach out using the form below")
    
    # Contact form fields
    name = st.text_input("Name*")
    email_id = st.text_input("Email-id*")
    mobile_number = st.text_input("Mobile Number*")
    message = st.text_input("Description")
    
    if st.button("Submit"):
        if name and email_id and message:
            st.success("Your request sent successfully ! Soon you reach the replay")
        else:
            st.error("Please fill all the Fields")
    
    st.subheader("Contact Details")

    # Bank Contact details
    st.write("📲 Mobile : +91 9385365443")
    st.write("☎️ Landline : 044-123456")
    st.write("📧 Email-id : babumani429@gmail.com")
    st.write("🌐 website : www.yrbankpvtltd.com")



