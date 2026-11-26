# Framework toolkit

Short guide to the frameworks named in SKILL.md: when to pick each, how to run it, and its common failure. Use the user's framework if they name one.

## Framing and structure

| Framework | Use when | How | Watch out for |
|---|---|---|---|
| Situation, complication, question, answer | Executive audience, unclear or political issue | One line each: stable situation, what changed, the question it raises, the proposed answer | Mixing the complication with a solution |
| Issue tree (MECE) | Big question, many possible causes | Split the question into branches that do not overlap and together cover it; go two or three levels | Overlapping branches, or a cut that does not help the decision |
| Hypothesis-driven analysis | Time is short, data is partial | State the likely answer first, list what would prove it wrong, test the cheapest item first | Collecting only confirming evidence |
| Problem variation | Stuck | Solve a simpler version, work backward from the goal, find an analogy, relax a constraint | Leaving the simplified answer unchecked against the real problem |
| Look-back step | After any solution | Check the result, derive it a second way, ask what else the method applies to | Skipping it under time pressure |

## Root-cause tools

| Tool | Use when | How |
|---|---|---|
| Five whys | One clear failure, a chain of causes | Ask why, answer with evidence, repeat until a cause you can act on; stop at a process or incentive, not at a person |
| Fishbone (cause-and-effect) | Many contributors | Group causes under categories such as people, process, tools, inputs, environment, measurement; test the top ones |
| Fault tree | Safety or reliability failure | Start from the failure, list the combinations of events that produce it |
| Compare with and without | Variables interact | Pick cases where the problem occurs and where it does not; list what differs |
| Change one variable | Test is cheap and reversible | Alter one factor at a time and observe |
| Feedback loops and delays | Fixes failed or the problem returns | Draw reinforcing and balancing loops; look for fixes that treat symptoms and weaken the real remedy |
| Leverage points | Deciding where to intervene | Rank interventions: tuning numbers is weak; changing information flows, rules, incentives or goals is stronger |

## Competitive and stakeholder dynamics

| Framework | How |
|---|---|
| Players, options, payoffs, information | List who acts, what each can do, what each gains or loses, who knows what |
| Payoff matrix and dominant option | Two players, few options; find any option that is best whatever the other does |
| Equilibrium check | For each outcome ask whether any player gains by changing alone; stable outcomes are likely |
| One-shot versus repeated | Repeated play rewards reputation and credible retaliation; one-shot rewards defection |
| Second-order thinking | For each option ask "and then what" for the other side, customers and your own team; note delayed and unintended effects |
| Inversion | Ask what would guarantee failure, then avoid it |

## Decide and act

| Framework | How |
|---|---|
| Decision matrix | Agree criteria, weights (sum 100), scores 1 to 5 with reasons; show how sensitive the winner is to the top weight |
| Reversible versus irreversible | Reversible: decide with roughly 70 percent of the information (reference point, adjust to risk). Irreversible: slow down, pilot, seek dissent |
| Scenario thinking | Two key uncertainties form a 2x2; describe each quadrant; pick moves that hold in most, plus early-warning signals |
| Pre-mortem | Assume failure at a set date; each person lists reasons; rank by likelihood and impact; add a preventive action to the plan |
| Observe, orient, decide, act loop | Fast-moving situations: shorten the cycle, update the picture of the situation after each action |
| Urgent-important matrix | Do now, schedule, delegate, drop; guard time for important but not urgent work |
| Design thinking | Empathise, define, ideate, prototype, test; use for customer or user problems before committing to a build |
| Disagree and commit | After debate, one owner decides and the group executes; write down the decision and the review date |
| Action planning | Action, owner, due date, deliverable, dependency; checkpoints with metric, threshold and continue-adjust-stop rule |

## Routing by problem type

| Situation | Sequence |
|---|---|
| Recurring operational failure | Frame, five whys or fishbone, loops, options, matrix, action plan |
| Competitor move | Players and payoffs, equilibrium, second-order check, scenarios, reversible decision |
| Stuck or too broad | Frame, issue tree, hypothesis, cheapest test |
| Feature or product nobody uses | Five whys, empathise and define, prototype, test, checkpoint on adoption |
| Crisis | Observe-orient-decide-act now, root cause after stabilising, communicate with the situation-complication frame |
| Too many priorities | Urgent-important matrix, decision matrix, drop list |

Reference points in this file are starting values. Check them against the user's own context.
