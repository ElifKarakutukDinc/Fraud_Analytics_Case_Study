# Fraud_Analytics_Case_Study

## Background:
There are three important metrics to remember when implementing fraud rules:

· % Hit Rate
o #/$ of fraud transactions hit by rule / #/$ of total transactions hit by rule
· % Catch Rate
o #/$ of fraud transactions hit by rule / #/$ of all fraud transactions
· % Rejection Rate
o #/$ of transactions rejected / #/$ of all attempted transactions

Fraud is a balance, so we want to try to maximize hit rate and catch rate, and minimize rejection
rate, when finding a good rule to put into place. You can assume that in this population, these
were all approved and completed orders, and the fraudulent transactions (EVENT_LABEL) were
detected after fulfillment.

Please provide a summary of the top 3-5 rules you would immediately implement if you were
building a fraud decision process for this population. You can use the variable as given, or
combine them as needed to make your own. Include the above metrics for each rule, and the
ruleset as a whole, as well as how you came to your conclusions.
