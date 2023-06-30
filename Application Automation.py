from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(
        "https://capri.wd1.myworkdayjobs.com/en-US/Michael_Kors/job/Stock-Associate-PT--Toronto-Eaton-Center_R_761493") 
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Apply Manually").click()

    page.get_by_label("Email Address").click()
    page.get_by_label("Email Address").fill("emamil5478@gmail.com")
    page.get_by_label("Email Address").press("Tab")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Decline").click()
    page.get_by_label("Password").fill("Your_high_profile_pasword^")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_load_state("networkidle")
    page.get_by_label("How Did You Hear About Us?*").click()
    page.wait_for_load_state("networkidle")
    page.get_by_text("LinkedIn").click()
    time.sleep(1)
    page.get_by_text("Networking with Recruiter").click()
    time.sleep(1)

    page.get_by_label("First Name*").click()
    page.get_by_label("First Name*").fill("Devesh")

    page.get_by_label("First Name*").press("Tab")
    page.get_by_label("Last Name*").fill("Premkumar")
    page.get_by_label("Address Line 1").click()
    page.get_by_label("Address Line 1").fill("Home adress")
    page.get_by_label("City").click()
    page.get_by_label("City").fill("Mississauga")
    page.get_by_role("button", name="Province or Territory select one").click()
    page.get_by_text("Ontario").click()
    page.get_by_label("Postal Code").click()
    page.get_by_label("Postal Code").fill("L5M 3C4")
    page.get_by_label("No").check()



    page.get_by_role("button", name="Phone Device Type select one required").click()
    page.get_by_role("option", name="Mobile").click()
    page.get_by_label("Phone Number*").click()
    page.get_by_label("Phone Number*").fill("(9058179688")
    page.get_by_role("button", name="Save and Continue").click()
    
    page.get_by_role("button", name="Add Education").click()
    page.get_by_label("School or University*").fill("St. Francis Xavier Secondary School")
    page.get_by_label("School or University*").press("Tab")
    page.get_by_role("button", name="Degree select one required").click()
    page.get_by_text("High School").click()
    page.get_by_placeholder("Search").click()
    page.get_by_label("Overall Result (GPA)").click()
    page.get_by_label("Overall Result (GPA)").fill("3.7")
    
    page.get_by_role("button", name="Add Languages").click()
    page.get_by_role("button", name="Language select one required").click()
    page.get_by_role("option", name="English").get_by_text("English").click()
    page.get_by_role("button", name="Overall Comprehension select one required").click()
    page.get_by_text("Fluent", exact=True).click()

    page.get_by_role("button", name="Reading select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Reading select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Speaking select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Writing select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
   
    page.get_by_role("button", name="Add Languages").click()
    page.get_by_role("button", name="Language select one required").click()
    page.get_by_role("option", name="French").get_by_text("French").click()
    page.get_by_role("button", name="Overall Comprehension select one required").click()
    page.get_by_text("Fluent", exact=True).click()
    page.get_by_role("button", name="Reading select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Speaking select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Writing select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    
    


    page.get_by_role("button", name="Add Another Languages").click()
    page.get_by_role("button", name="Language select one required").click()
    page.get_by_text("Tamil").click()
    page.locator("#input-35").check()
    page.get_by_role("button", name="Overall Comprehension select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Reading select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Speaking select one required").click()
    page.get_by_role("option", name="Fluent").get_by_text("Fluent").click()
    page.get_by_role("button", name="Writing select one required").click()
    page.get_by_role("option", name="Fluent").click()

    page.get_by_role("button", name="Upload a file (5MB max)").click()
    page.get_by_role("button", name="Upload a file (5MB max)").set_input_files("Devesh Resume HSfinal(9).pdf")

    page.get_by_role("button", name="Add Websites").click()
    page.get_by_label("URL*").click()
    page.get_by_label("URL*").click()
    page.get_by_label("URL*").fill("https://www.linkedin.com/in/devesh-premkumar-6b979222b/")
    
    page.get_by_role("button", name="Save and Continue").click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="\"Are you at least 18 years of age?Avez-vous au moins 18 ans?\" select one required").click()
    page.get_by_role("option", name="Yes/Oui").get_by_text("Yes/Oui").click()
    page.get_by_role("button", name="The highest level of education I have attained is:Le niveau le plus haut d'éducation que j'ai atteint est: select one").click()
    page.get_by_text("High school diploma or equivalent Diplôme d'études secondaires ou équivalent").click()
    page.get_by_role("button", name="Do you have work authorization to work in the country you are applying for a position in?Avez-vous l'autorisation de travailler dans le pays dans lequel vous appliquez pour un poste? select one required").click()
    page.get_by_role("option", name="Yes/Oui").get_by_text("Yes/Oui").click()
    page.get_by_role("button", name="Will you now or in the future require sponsorship for employment?Auriez-vous besoin de parrainage pour vous permettre de travailler maintenant ou dans le futur? select one required").click()
    page.get_by_role("option", name="No/Non").get_by_text("No/Non").click()
    
    page.get_by_label("Please provide your base salary expectations in your local currency and any other components.Veuillez indiquer vos attentes salariales de base dans votre devise locale et dans tout autre élément.*").click()
    page.get_by_label("Please provide your base salary expectations in your local currency and any other components.Veuillez indiquer vos attentes salariales de base dans votre devise locale et dans tout autre élément.*").fill("15")
    page.get_by_label("Full-Time (30+ hours/week)  Temps plein (30+/heures par semaine)").check()
    page.get_by_label("Part-Time (0-29 hours/week)  Temps partiel (0-29/heures par semaine").check()
    page.get_by_label("Seasonal (Holiday/Summer)  Saisonnier (Été/Temps des fêtes)").check()
   

    page.get_by_label("Have you ever applied for employment with Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? If so, please state position applied for and location.Avez-vous déjà appliqué sur un poste chez Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? Si oui, veuillez indiquer le poste ainsi que l'endroit où vous avez appliqué.*").fill("no")
    page.get_by_label("Have you ever supplied services to Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? If so, please indicate dates, location and services provided.Avez-vous déjà fourni des services à Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? Si oui, veuillez indiquer les dates, l'endroit ainsi que les services fournis.*").fill("n")
    page.get_by_label("Have you ever supplied services to Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? If so, please indicate dates, location and services provided.Avez-vous déjà fourni des services à Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? Si oui, veuillez indiquer les dates, l'endroit ainsi que les services fournis.*").click()
    page.get_by_label("Have you ever supplied services to Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? If so, please indicate dates, location and services provided.Avez-vous déjà fourni des services à Capri Holdings Limited (Versace, Jimmy Choo, Michael Kors)? Si oui, veuillez indiquer les dates, l'endroit ainsi que les services fournis.*").fill("no")
    page.get_by_label("Do you have a current non-compete agreement? If yes, please provide details.Avez-vous présentement une convention de non-concurrence? Si oui,veuillez fournir des détails.*").click()
    page.get_by_label("Do you have a current non-compete agreement? If yes, please provide details.Avez-vous présentement une convention de non-concurrence? Si oui,veuillez fournir des détails.*").fill("no")
    page.get_by_label("Have you previously been employed under any other legal name(s)?  Please indicate yes or no.   If yes, please provide name(s)Avez-vous déjà été embauché sous un autre nom légal? Veuillez indiquer oui ou non. Si oui, veuillez inscrire le/les nom (s).*").click()
    page.get_by_label("Have you previously been employed under any other legal name(s)?  Please indicate yes or no.   If yes, please provide name(s)Avez-vous déjà été embauché sous un autre nom légal? Veuillez indiquer oui ou non. Si oui, veuillez inscrire le/les nom (s).*").fill("no")
    page.get_by_label("Have you ever been discharged, forced to resign, or otherwise been involuntarily terminated? If yes, please provide detailsAvez-vous déjà été libéré, forcé à démissionner ou terminé involontairement? Si oui, veuillez fournir des détails.*").click()
    page.get_by_label("Have you ever been discharged, forced to resign, or otherwise been involuntarily terminated? If yes, please provide detailsAvez-vous déjà été libéré, forcé à démissionner ou terminé involontairement? Si oui, veuillez fournir des détails.*").fill("no")
   

    page.get_by_role("spinbutton", name="Month").fill("06")
    page.get_by_role("spinbutton", name="Day").fill("27")
    page.get_by_role("spinbutton", name="Year").fill("2023")



    page.get_by_role("button", name="Save and Continue").click()
    page.wait_for_load_state("networkidle")
    page.get_by_label("Monday Morning").check()
    page.get_by_label("Monday Afternoon").check()
    page.get_by_label("Monday Evening").check()
    page.get_by_label("Tuesday Morning").check()
    page.get_by_label("Tuesday Afternoon").check()
    page.get_by_label("Tuesday Evening").check()
    page.get_by_role("row", name="Wednesday Morning").click()
    page.get_by_label("Sunday Evening").check()
    page.get_by_label("Sunday Afternoon").check()
    page.get_by_label("Sunday Morning").check()
    page.get_by_label("Saturday Evening").check()
    page.get_by_label("Saturday Afternoon").check()
    page.get_by_label("Saturday Morning").check()
    page.get_by_label("Friday Evening").check()
    page.get_by_label("Friday Afternoon").check()
    page.get_by_label("Friday Morning").check()
    page.get_by_label("Thursday Evening").check()
    page.get_by_label("Thursday Afternoon").check()
    page.get_by_label("Thursday Morning").check()
    page.get_by_label("Wednesday Evening").check()
    page.get_by_label("Wednesday Afternoon").check()
    page.get_by_role("button", name="Save and Continue").click()
    time.sleep(5)
    page.get_by_label("Yes, I have read and consent to the terms and conditions*").check()
    page.get_by_role("button", name="Save and Continue").click()
 
    
    print("application ready for Review auto sumbting in 20")
    
    time.sleep(20)

    page.get_by_role("button", name="Submit").click()


    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
