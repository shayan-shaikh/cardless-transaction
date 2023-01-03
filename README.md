

VISVESVARAYA TECHNOLOGICAL UNIVERSITY
Jnana Sangama, Machhe, Belagavi-590018
 

A Project Report                             On
      “Eliminating the physical layer of cards whilst increasing the accessibility in a cash transaction.”
Submitted in fulfillment required in respect to
AccelATHON 3.0
Computer Science and Engineering
6th Semester
Submitted by
BASAVARAJ	 1HK19CS032
                                                    SAMI IBRAHIM                                1HK19CS130
SHAYAN SHAIKH                            1HK19CS139
SONAM DORJI                                1HK19CS150
SYED TAJAMUL SHAH	1HK19CS167                                           
Under the guidance of
Prof.  SONIA D’SOUZA
Assistant Professor
Department of Computer Science & Engineering
                                                        2021-2022
 
                            Department of Computer Science & Engineering
HKBK COLLEGE of ENGINEERING
       (Approved by AICTE & Affiliated to VTU)
                                       22/1, Nagawara, Arabic College Post, Bangalore-45, Karnataka
Email: info@hkbk.edu.in URL: www.hkbk.edu.in
 
### ACKNOWLEDGEMENT


We would like to express our regards and acknowledgement to all who helped us in completing this project successfully.
First of all, we would take this opportunity to express our heartfelt gratitude  and  regards  to Mr. C M Ibrahim, Chairman, HKBKGI and Mr. Faiz Mohammed, Director, HKBKGI for providing facilities throughout the course.
We express our sincere gratitude to Prof. Tabassum Ara, Principal, HKBKCE, for his support towards the attainment of knowledge.
We consider it as a great privilege to convey our sincere regards to Dr. Loganathan. R., Professor and HOD, Department of CSE, HKBKCE for his constant encouragement throughout the course of the project.
We would specially like to thank our guide, Prof. Sonia D’Souza, Assistant Professor, Department of CSE for her vigilant supervision and her constant encouragement. She spent her precious time in reviewing the project and provided many insightful comments and constructive criticism.
Finally, we thank Almighty, all the staff members of CSE Department, our family members and friends for their constant support and encouragement in carrying out the Project work.


BASAVARAJ                                     1HK19CS032                                                    SAMI IBRAHIM                                1HK19CS130
SHAYAN SHAIKH                            1HK19CS139
SONAM DORJI                                 1HK19CS150
SYED TAJAMUL SHAH	                 1HK19CS167






### ABSTRACT

In the era of internet, most of the people all over the world complete their transaction on internet via payment apps and websites. However, there is still a vast number of people who complete their day-to-day transactions through physical cards. Though the user of electronic transaction or E-money transaction system increase rapidly but the majority of people are concerned about the security of this system. The growth in online transactions has resulted in a greater demand for fast and accurate user identification and authentication. There is a glaring problem of accessibility in such cases wherein the user doesn’t have a physical card present with him/her. For such cases and scenarios where the need for physical cards is a hassle posing for a user, we have designed a model that would reduce the altogether need of such scenarios as well as increasing the accessibility by increasing the reliance and pacing of a transaction.






















### CONTENTS



Acknowledgement                    								i                                                                        
Abstract					                               				ii   
Contents                                                                                                                        iii
1.	Objective & Scope of the Project							1                                                             
2.	Theoretical Background								3                                                                     
3.	Definition of Problem									4                                                                            
4.	Feasibility Study                                                                                                           5
5.	System analysis & planning v/s user requirement				            7                                                               
6.	System Planning (PERT Chart)							            13                                                                       
7.	Methodology adopted; System Implementation & Details of H/W& S/W used	14                                                                 
8.	Detailed Life Cycle of the Project							15                                                              
9.	ERD, DFD										17
10.	Input and Output Screen Design (Snapshots)						23
11.	Source Code						                         		26
12.	Future Enhancements						                                    33 Conclusion                                                                                                                                  References		



### INTRODUCTION
Today the regional economies, societies, cultures and educations are integrated through a globe-spanning network of communication and trade. Today’s most of business dealings (order receive, delivery confirmation, transaction and business communication) are done on internet. Rapid development of banking technology, Banks provide facilities to their client to transaction their money from an account through a security system using internet. This system is known as electronic transaction. Notwithstanding, we have lived in a world where people no longer want to encounter long queues for any reasons and this has led to the increasing services being rendered by banks to further improve the convenience of banking through the means of electronic banking. The growing rate of the popularity of electronic transaction has increased day by day. Now-a-days most of the people make their banking activities such as cash withdrawal, money transfer, paying phone and electricity bills, online purchase beyond official hours without physical interaction with bank staff, using internet. Banks have fascinated their customers to carry out banking transactions like deposits, transfers, balance enquiries, mini statement, withdrawal and fast cash etc. in various ways. 
There are two ways a customer can perform their banking activities. First one, physically, by interacting with banking staff and second one is electronic transaction (ATM transaction, online transaction and E-coin). For the first case bank staff manually authenticates a user based on check book, customer signature and photo. In the case of electronic transaction bank follows conventional method where authenticate a user based on user id and PIN (personal identification number). But in this case security and accessibility are the major issues regarding electronic transaction. 
For these case scenarios wherein, a user doesn’t have a physical card present and is required to pay for a service, we have devised a model where the user can obtain easy cash withdrawal from any nearby ATM or any retailer by just presenting with a QR code which can be scanned by the scanner present with the retailer. This model allows full autonomy to the user to obtain cash by easy access method without the use of any physical card. Also, by allowing full control to the user, the model allows the added advantage of transparency as well as increased security. This method allows the discouragement of the use of phishing methods in normal ATM kiosks as well as any malpractice by any retailer in cash handling.

### OBJECTIVE & SCOPE
##### 2.1 Objective 
	The main objective of this model is to provide more rapid accessibility to a user by providing a more rapid and efficient way of obtaining cash without the need of an actual physical card to be present on the person. This aims to reduce the hassle of carrying a physical card at all times as well as the security risk of online transactions by providing an alternative method involving cash for the traditional users. Another objective is to introduce more strengthened layers of security in this model to further bolster its reliability as well as reduce the risks of any malpractice.
##### 2.2 Scope
	The model is helpful for any domain with respect to transactions particularly the retail sector of the society where the need of cash is paramount for any traditional user. Furthermore, the sectors of rapid payment through e-transactions can benefit from this domain as well by implementation of this model for e-payment.
	Nevertheless, with some further bolstering with additional modules like voice authentication, SOS generation and many other services, the model can prove to be a game changing method for any type of transaction anywhere.


### THEORETICAL BACKGROUND

Problems in existing system:
•	Service fees:
Payment gateways and third-party payment processors charge service fees.

•	Inconvenient for offline sales:
Online payment methods are inconvenient for offline sales.

•	Vulnerability to cybercriminals:
Cybercriminals can disable online payment methods or exploit them to steal people’s money or information. 

•	Reliance on telecommunication infrastructure:
Internet and server problems can disable online payment methods.

•	Technical problems:
Online payment methods can go down due to technical problems.

•	Disputed Transactions:
Without sufficient information about the fraudulent person who performed the transaction, though, it can be difficult to win the claim and receive a refund.
•	Increased Business Costs:
E-payment systems come with an increased need to protect sensitive financial information stored in a business's computer systems from unauthorized access. Enterprises with in-house e-payment systems must incur additional costs in procuring, installing and maintaining sophisticated payment-security technologies.

Solution to these problems: 
•	No service fees charged as the hosting is done by the user and thus no item needs a third-party service.

•	The model can be used for both offline and online sales as we have this model designed for both sales as well as users.


•	No major vulnerability to cyber crime as the model does not rely on traditional methods of transactions due to its unorthodox nature. Also, the QR code generation is user based and the scanning of the code is business based and thus doesn’t rely on any traditional pathways that could be exploited for any nefarious purposes.

•	Business costs are low because no additional hosting is required by the business.


### PROBLEM DEFINITION
The problem is the requirement of physical cards or any offline transaction as well as the requirement of hard cash. Here the model explores the elimination of the physical layer of cards whilst increasing the accessibility in a cash transaction. Also the model implementation can be useful for any online transaction as well.


### TECHNICAL, ECONOMICAL & OPERATIONAL FEASIBILITY

5.1 Types of Feasibility:
1.	Financial feasibility:
Financial feasibility refers to financial support required. It refers to finance incurred during the development of the project.

2.	Technical feasibility:
Technical feasibility refers to technical knowhow and auxiliary devices required.

3.	Behavioural feasibility:
Refers to reaction of the people towards the project.

4.	Operational feasibility:
Operational feasibility means is it possible to practically implement the project. While installing this software, the hardware and software requirements should be specified.

5.2 FEASIBILITY GAINED BY OUR SYSTEM:
Technical Feasibility
		Since our project is in Python and CSV so we need to have a strong base in programming. 

Economic Feasibility
		To implement the system, we require more than one operational device. Since the system will be implemented in existing environment there will be no need to buy the computers. The system is economically feasible to implement.

Operational Feasibility
		Our system will be easy to install and use. Hence our system is operationally feasible.

Cost-Benefit Analysis
		The cost incurred by our system includes only the software cost and cost of the device needed to run the project.
 
### SYSTEM ANALYSIS & PLANNING
6.1 Analysis Model
	This document plays a vital role in the development of life cycle (SDLC) as it describes the complete requirement of the system.  It means for use by developers and will be the basic during testing phase.  Any changes made to the requirements in the future will have to go through formal change approval process.
	SPIRAL MODEL was defined by Barry Boehm in his 1988 article, “A spiral Model of Software Development and Enhancement.  This model was not the first model to discuss iterative development, but it was the first model to explain why the iteration models.
	As originally envisioned, the iterations were typically 6 months to 2 years long.  Each phase starts with a design goal and ends with a client reviewing the progress thus far.   Analysis and engineering efforts are applied at each phase of the project, with an eye toward the end goal of the project. 
The steps for Spiral Model can be generalized as follows:
•	The new system requirements are defined in as much details as possible.  This usually involves interviewing a number of users representing all the external or internal users and other aspects of the existing system.
•	A preliminary design is created for the new system.
•	A first prototype of the new system is constructed from the preliminary design.  This is usually a scaled-down system, and represents an approximation of the characteristics of the final product.
•	A second prototype is evolved by a fourfold procedure:
1.	Evaluating the first prototype in terms of its strengths, weakness, and risks.
2.	Defining the requirements of the second prototype.
3.	Planning and designing the second prototype.
4.	Constructing and testing the second prototype.


•	At the customer option, the entire project can be aborted if the risk is deemed too great.  Risk factors might involve development cost overruns, operating-cost miscalculation, or any other factor that could, in the customer’s judgment, result in a less-than-satisfactory final product.
•	The existing prototype is evaluated in the same manner as was the previous prototype, and if necessary, another prototype is developed from it according to the fourfold procedure outlined above.
•	The preceding steps are iterated until the customer is satisfied that the refined prototype represents the final product desired.
•	The final system is constructed, based on the refined prototype.
•	The final system is thoroughly evaluated and tested.   Routine maintenance is carried on a continuing basis to prevent large scale failures and to minimize down time. 
The following diagram shows how a spiral model act like:


 
                                                                 Fig 5.2 : Spiral Model 
6.2 Study of the System:
6.2.1 Graphical user interface
	In the flexibility of the uses the interface has been developed a graphics concept in mind, associated through a browser interface. The GUI’S at the top level have been categorized as
1.	Administrative user interface
2.	The operational or generic user interface
	The administrative user interface concentrates on the consistent information that is practically, part of the organizational activities and which needs proper authentication for the data collection. The interfaces help the administrations with all the transactional states like Data insertion, Data deletion and Date updation along with the extensive data search capabilities.
	The operational or generic user interface helps the users upon the system in transactions through the existing data and required services. The operational user interface also helps the ordinary users in managing their own information helps the ordinary users in managing their own information in a customized manner as per the assisted flexibilities.


### SYSTEM PLANNING (PERT CHART)

	Perform and evaluate feasibility studies like cost-benefit analysis, technical feasibility, time feasibility and operational feasibility for the project. Project Scheduling should be made using PERT charts.
	Feasibility study is carried out to decide whether the proposed system is feasible for the company. The feasibility study is to serve as a decision document it must answer three key questions:
1.	Is there a new and better way to do the job that will benefit the user?
2.	What are the cost and the savings of the alternative(s)?
3.	What is recommended?

Technical feasibility:
Technical feasibility centers on the existing computer system i.e., Hardware, Software etc. Bank requires SQL database management that are all easily available with extensive development support through manuals and blogs. 

Economical feasibility:
Economical Feasibility is the most frequently used method for evaluating the effectiveness of a candidate system. More commonly known as Cost/ Benefit analysis, the procedure is to determine the benefits and savings that are expected from the candidate system and compare them with costs. If the benefits outweigh costs, then the decision is made to design and implement the system.



### METHODOLOGY ADOPTED, SYSTEM IMPLEMENTATION & DETAILS of HARDWARE & SOFTWARE USED

7.1 Methodology adopted and System implementation:
•	Apache tomcat is used as a web server to host the application.
•	All the environment variables are set.
•	The application is pasted in the webapps folder.
•	Web server is started now.
•	Application is run using the web browser by typing http://localhost/cis
•	Web.xml file is used to control the flow and user actions.

7.2 Details of hardware & software used:
Hardware Specification (Minimum):

		Disc Space:             	40 GB
		PC Used:                 	IBM Compatible
		Processor:      	            Pentium 3
		Memory: 	            512 MB RAM
		File System:            	32 Bit

Software Specification:

		Operating System (Server Side):	Windows 11.
Operating System (Client Side):      Windows 11.
Client End Language:                       HTML
Local Validation: 			 PHP
Server-Side Language: 		 PHP
Database: 				 My Sql 2000
Web Server: 				 XAMPP server
                        Web Browser:	                         Google Chrome/ Mozilla Firefox



### DETAILED LIFE CYCLE OF PROJECT

          	We have used Waterfall Model as Software Engineering life Cycle Process. It is the simplest; oldest and most widely used process model for software development. This model acquires its name from the fact that classic software life cycle is represented as a sequence of descending steps.
 
Fig 8.1 : Waterfall Model 
8.1 Requirement Analysis:
	This process is also known as feasibility study. In this phase, the development team studied the site requirement. They investigate the need for possible dynamic representation of the site and increase security features. By the end of feasibility study, the team furnishes a document that holds the different specific recommendations for the candidate system. It also includes personnel assignments, costs, project schedules, target dates etc. the requirement gathering process is intensified and focused specially on software. The essential purpose of this phase is to find the need and to define the problem that needs to be solved. During this phase following facts were gathered.
	Determined the user need
	Establish the goals and objective for the proposed system
	Feasibility for the new system
8.2 System Analysis and Design:
        	In this phase the software’s overall structure and its nuances are defined. In terms of client server technology, the no of tiers needed for the package architecture, database design, data structure design etc are defined in this phase. Analysis and Design are very crucial in entire development cycle. Any glitch in this phase could be expensive to solve in the later stage of software development. Hence following is the essential approach taken during website designing:
	DFD
	Database Designing
	Form Designing
	Pseudo code for methods
8.3 Testing:
         	Once the code is generated, the website testing begins. Different testing methodologies are done to unravel the bugs that were committed during the previous phases. Different testing methodologies are used:
	Acceptance Testing
	White Box Testing
	Black Box Testing

#### FUTURE ENHANCEMENTS
•	Introduction of SSL encryption layer in transaction to ensure authentication as well as increased security.
•	Introduction of voice recognition, biometric authentication as well as SOS generation for enhanced security of the system.
•	Implementation of the system on large scale to reduce the initial cost of setup and general accessibility.
