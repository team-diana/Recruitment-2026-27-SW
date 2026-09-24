# S.A.F.E. Code

Year 3023. Team DIANA is again trying to participate in URC, but now they are more motivated than ever. Last year, during the last test before departure, our three AI agents that operate the rover were arguing about something: St-3 was sure that the place where they were at the moment was perfect for drilling, while Ann-4 and M4-TT3 wanted to move further. As a result, the rover was drilling while moving, so it broke...

In order to avoid this, our team of engineers decided to implement a system to ensure that these events would no longer be replicable. However, they don't want to ask an AI to solve this problem (because they could argue during coding too), so they tried to do it by themselves. Unfortunately, they are no longer capable of coding. Can you help them?

## Challenge rules
You are asked to implement a system to ensure the rover will follow the rules written below. Once done, veirfy for each string in the `"Input_States.txt"` if it is valid or not, and provide as output a file with the results. 

### 1. The Rover's 6 Moods (States)

* **`B` (Boot):** Waking up, running self-tests, and checking instruments. The rover always starts in this state.
* **`I` (Idle):** Parked and chilling, awaiting mission dispatch commands.
* **`N` (Navigating):** Rolling across the surface. Wheels turning; all science gear must stay safely stowed.
* **`S` (Sampling):** Light science mode. Sniffing dust, analyzing ambient air, and taking camera panoramas.
* **`C` (Core Drilling):** Heavy-duty corer driven deep into bedrock. **The rover must not move a single millimeter.**
* **`F` (Fault):** Emergency safe mode. Plays dead and waits for Houston/Earth to intervene.

---

### 2. Command Alphabet

* **`'O'` (OK):** *"All systems green, ready to roll."*
* **`'G'` (Go):** *"Hit the gas!"*
* **`'A'` (Analyze):** *"Start surface sampling."*
* **`'K'` (Kore / Core):** *"Deploy the core drill and extract a rock core!"*
* **`'D'` (Done):** *"Operation complete; stow gear and return to standby."*
* **`'E'` (Emergency):** *"Red alert! Critical hardware anomaly!"*
* **`'R'` (Reset):** *"Turn it off and on again."* (Ground control override).

---

### 3. Transition Matrix

If an action says **`NOPE`**, the rover outright rejects the command to preserve hardware integrity.

| State | Input `'O'` | Input `'G'` | Input `'A'` | Input `'K'` | Input `'D'` | Input `'E'` | Input `'R'` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`B`** (Boot) | **`I`** | `NOPE` | `NOPE` | `NOPE` | `NOPE` | **`F`** | `NOPE` |
| **`I`** (Idle) | `NOPE` | **`N`** | **`S`** | **`C`** | `NOPE` | **`F`** | `NOPE` |
| **`N`** (Navigating) | `NOPE` | `NOPE` | `NOPE` | `NOPE` | **`I`** | **`F`** | `NOPE` |
| **`S`** (Sampling) | `NOPE` | `NOPE` | `NOPE` | `NOPE` | **`I`** | **`F`** | `NOPE` |
| **`C`** (Core Drilling) | `NOPE` | `NOPE` | `NOPE` | `NOPE` | **`I`** | **`F`** | `NOPE` |
| **`F`** (Fault) | `NOPE` | `NOPE` | `NOPE` | `NOPE` | `NOPE` | `NOPE` | **`B`** |

---

### 4. Delivery Instructions

In the file `"Input_States.txt"` there is a list of possible inputs for the rover, used to validate the algorithm. Provide the code you used to validate these strings and a file in which, for each string, you state whether it is valid or not, following this structure:

Input file:
- 1. OAKDE
- 2. OGDCDER
- ...

Output file:
- 1. Not Valid
- 2. Valid
- ...

## Challenge Score
Total Score: 300