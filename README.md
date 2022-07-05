# Fraud_Analytics_Case_Study

## Background:

There are three important metrics to remember when implementing fraud rules:

· % Hit Rate

fraud transactions hit by rule / total transactions hit by rule

· % Catch Rate

fraud transactions hit by rule / all fraud transactions

· % Rejection Rate

transactions rejected / all attempted transactions

Fraud is a balance, so we want to try to maximize hit rate and catch rate, and minimize rejection
rate, when finding a good rule to put into place. You can assume that in this population, these
were all approved and completed orders, and the fraudulent transactions (EVENT_LABEL) were
detected after fulfillment.
