**Problem:**
Organizing a Secret Santa event for Easter can be an enjoyable endeavor. However, manually assigning participants to one another and communicating their matches can be tedious and prone to errors. Additionally, maintaining secrecy and fairness throughout the assignment process presents its own set of challenges.

**Solution:**
The "Easter Bunny Secret Santa" program offers an automated solution to address these issues. It enables event organizers to input the names and email addresses of participants, after which it randomly assigns each participant a Secret Santa recipient. The program handles this assignment process securely and efficiently, ensuring that each participant receives their match without any knowledge of who else is participating or who their Secret Santa is. Furthermore, the program sends personalized emails to each participant, notifying them of their assigned recipient. This not only streamlines the communication process but also enhances the festive ambiance of the event. Overall, the program simplifies the organization of Easter-themed Secret Santa events, providing a hassle-free and enjoyable experience for all involved.

**Syntax:**
```bash
python easter.py```

**How to Use:**

1. Configure the SMTP email settings with your login and password. Currently, the program is set to use a Google account named easterbunny568@gmail.com and its corresponding Google app password. You can configure any email account of your choice. Note: While the keys are public, this practice is not recommended and should be revised in the future.
2. Check out the easter_bunny.py file.
3. Ensure that Python 3 is installed on your system.
4. Make sure Python is added to your Windows PATH.
5. Open the Command Prompt (CMD).
6. Navigate to the directory where you downloaded the program.
7. Run the command: python easter_bunny.py.
8.Follow the prompts to input the quantity of guests, along with their names and email addresses.
9.Once all information is provided, emails will be sent out.

Note: It's currently not possible to edit the email of a participant, but this feature may be implemented in the future.
