BASE_URL = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
FIRST_NAME  = ""
LAST_NAME = ""
PHONE = ""
USER_ID = FIRST_NAME + LAST_NAME[0] + PHONE[:3]
PASSWORD = LAST_NAME + FIRST_NAME[0] + "@321"
