# MSMPIFSG Design Doc
a System Preformance Troubleshooting Toolkit by *Andrew Dettor & Logan Mimaroglu*

### Overview
This program is being developed so that the average person can run the application and determine wether or not they need to upgrade there computer, and if they do, what specifically they should upgrade. The program will be comprised of three parts. 

The first part of the program is the GUI. Here, the user should be able to input benchmarking information for the program to evulate the results of and return wether or not the computer fits the users needs. If the program determines the computer does not fit the users needs, then it should call on the second part of the program. 

The second part of the program should gather computer parts and determine which part(s) should be upgraded inorder to improve performance. During this time, the program will also check to see if the parts that the user has are adequate but are just under performing. If the computer is underperforming realitve to a standard, the program should call the third part. 

The third part should attempt to troubleshoot why the PC is underperforming and implement fixes. This could include running registry checks, memory tests, recommending more drastic action like resetting the OS. 

### Context
The IDC predicts that over 2.4 trillion dollars on technology in 2018 and that 74% of this is on upgrading existing technology. However, no tool exists for determining whether upgrading a slow computer or phone is justified. Nor for seeing if the technology can be sped up without upgrading it.

### Goals and Non-Goals
- Accuretly sort a computer into one of three categories
   1. Browsing
   2. Gaming
   3. Workstation
- Offer the correct recommedations for computer part upgrades relative to it's category
- Detect and fix performance issues that are within the scope of the OS (i.e., more than hardware recommedations)

### Proposed Solution
Use pre-existing benchmarking software to evalaute the computer preformance relative to other systems. However, the identification of the PC and preformance optimazations will be programmed in house. 

- Pros
  - Use cutting edge software that has spent years in developement
  - Access to a massive online database of other computers
- Cons
  - Can never sell the product because of copyright reasons*

### Alternative Solution
Develop the benchmarking software in-house
- Pros
  - Avoid copyright strike
- Cons
  - Not really pratical as it would take years and signficantly more CS knowledge than the devs posses

### Testing Methods
Part 1: Identification
1. Run program on a computer which has already been defined as a browsing, gaming, or workstation computer.
2. Compare the experimental reutnr value of the program to the actual value given to it.
3. Compare the two values to see if they match. A match represents a success. A non-match represents a failure. 

Part 2: Comparison
1. Run program on a computer which has been purposely filled with bloat ware, a bad memory stick, and drive at or near maximum capacity. 
2. Compare the results

Part 3: Improvement
1. Run Passmark Benchmarking Software on a clean OS.
2. Fill OS with bloat ware, a bad memory stick, and drive at or near maximum capacity.
3. Run PassMark Benchmarking Software again.
4. Run program.
5. Run PassMark Benchmarking Software again.
6. Compare final results to the initial and intermediate results to see how well the program cleaned up the OS.

### User Story
TBD

### Timeline
n/a

### Milestones
Date: 2/20/2019
Summary: The computer program is able to accurtely identify computers as one of the three categories. It is also able to offer hardware recommendations, however, because of faulty string comparisons, it sometimes recommends parts the user already has. 
