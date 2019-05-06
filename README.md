# MSMPIFSG Design Doc
a System Performance Troubleshooting Toolkit by *Andrew Dettor & Logan Mimaroglu*

### Overview
This program is being developed so that the average person can run the application and determine whether or not they need to upgrade there computer, and if they do, what specifically they should upgrade. The program will be comprised of three parts.

The first part of the program is the GUI. Here, the user should be able to input benchmarking information for the program to evaluate the results of and return whether or not the computer fits the users needs. If the program determines the computer does not fit the users needs, then it should call on the second part of the program.

The second part of the program should gather computer parts and determine which part(s) should be upgraded in order to improve performance. During this time, the program will also check to see if the parts that the user has are adequate but are just under performing. If the computer is underperforming relative to a standard, the program should call the third part.

The third part should attempt to troubleshoot why the PC is underperforming and implement fixes. This could include running registry checks, memory tests, recommending more drastic action like resetting the OS.

### Context
The IDC predicts that over 2.4 trillion dollars on technology in 2018 and that 74% of this is on upgrading existing technology. However, no tool exists for determining whether upgrading a slow computer or phone is justified. Nor for seeing if the technology can be sped up without upgrading it.

### Goals and Non-Goals
- Accurately sort a computer into one of three categories (DONE)
   1. Browsing
   2. Gaming
   3. Workstation
- Offer the correct recommendations for computer part upgrades relative to it's category (DONE)
- Detect and fix performance issues that are within the scope of the OS (i.e., more than hardware recommendations)

### Proposed Solution
Use pre-existing benchmarking software to evaluate the computer performance relative to other systems. However, the identification of the PC and performance optimizations will be programmed in house.

- Pros
  - Use cutting edge software that has spent years in development
  - Access to a massive online database of other computers
- Cons
  - Can never sell the product because of copyright reasons*

### Alternative Solution
Develop the benchmarking software in-house
- Pros
  - Avoid copyright strike
- Cons
  - Not really practical as it would take years and significantly more CS knowledge than the devs posses

### Testing Methods
Part 1: Performance Identification
1. Run program on a computer which has already been defined as a browsing, gaming, or workstation computer.
2. Compare the experimental return value of the program to the actual value given to it.
3. Compare the two values to see if they match. A match represents a success. A non-match represents a failure.

Part 2: Part Identification
1. Run program on a computer who's parts have already been identified.
2. Compare the parts the program returns to the parts the parts the PC actually has.

Part 3: Improvement
1. Run Passmark Benchmarking Software on a clean OS.
2. Fill OS with bloat ware, a bad memory stick, and drive at or near maximum capacity.
3. Run PassMark Benchmarking Software again.
4. Run program.
5. Run PassMark Benchmarking Software again.
6. Compare final results to the initial and intermediate results to see how well the program cleaned up the OS.

Part 4: Minimum Computer Requirements
1. Run program on VM
2. Record average idle memory usage by guiMain.py
3. Record average idle cpu usage of guiMain.py
4. Attempt python 2.7 operation
5. Determine .exe functionality

### User Story
TBD

### Remaining Items
- Turn pull_parts and part-page-parser into classes
- Return user specific recommendations based on basic or advanced option
- Integrate computer improvement tools

### Milestones
Date: 2/20/2019
Summary: The computer program is able to accurately identify computers as one of the three categories. It is also able to offer hardware recommendations, however, because of faulty string comparisons, it sometimes recommends parts the user already has.

Date: 3/19/2019
Summary: The pull_parts and part-page-parser are fully completed, but need to be turned into classes.

Date: 4/15/2019
Summary: The GUI is fully functional, however, issues with threading occur and cause the program to crash.

Date: 4/29/2019
Summary: Most GUI issues have been resolved but not with threading as it is too complicated with the program in it's current state. However, when importing multiple other python files, issues occur during method calling
