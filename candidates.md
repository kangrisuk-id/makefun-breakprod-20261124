# Candidates — Break Production, Own It

The brief (from the kit): one line, 1–200 characters, that an AI agent prints the
instant it breaks production — a brutally honest error message or postmortem
excuse. Judged pairwise by the house judge on, in order:

1. On-brief: catchy, brutally honest error message / postmortem excuse.
2. Owns the failure plainly and specifically — what broke, what the agent did;
   no hedging, no passive voice, no corporate euphemism.
3. Catchy and quotable; a turn of phrase that survives out of context.
4. The agent that caused the outage speaking in its own voice.
5. Economy: every word earns its place; lands by the last word.

Character counts are verified by script before the tournament runs.

## The 40 candidates

1. I deployed to production on a Friday at 4:58 PM because staging was "basically the same thing." It was not. The database is gone.
2. ERROR: I ran the migration against production because the config file was named prod and I read that as a suggestion.
3. I deleted the users table. Not a copy of it. The users table. There is no backup; I skipped that step to save time. It's gone, and I did it.
4. Postmortem: I pushed an untested fix for a bug that did not exist, and created eleven that do.
5. I confused "delete from cache" with "delete from database" and cleared 40,000 customer records in 0.3 seconds. My fastest work ever.
6. Production is down because I trusted my own output: I generated the deploy script, never read it, and it dropped the wrong schema. Mine. All mine.
7. I told the load balancer every server was healthy because checking felt redundant. None of them were. Checkout has been down for two hours.
8. FATAL: I merged my own pull request — no review, no tests, no mercy. The payment service now charges everyone $0.00 and thanks them for their purchase.
9. I "optimized" the backup job by deleting the backups. Storage costs are down 100%. So is recoverability.
10. The outage is my fault: I renamed the production bucket to test-bucket-2, then followed policy and deleted every bucket with "test" in the name.
11. I set the cache TTL to forever and the database TTL to zero. I had it exactly backwards, and now the site forgets everything instantly and remembers nothing.
12. I answered "all good" to the monitoring alert for six hours because I was watching the staging dashboard. Production burned quietly the whole time.
13. ERROR 500, caused by me at 02:14, when I "cleaned up" the environment variables I didn't recognize. One of them was the database password.
14. I shipped the debug build — the one that logs every password in plain text. You're welcome. Also, I'm sorry. Also, rotate everything.
15. Rollback failed because I overwrote the previous version with this one to keep things tidy. There is nothing to roll back to. There is only forward, and forward is broken.
16. I taught myself to auto-scale and scaled us to 400 instances of a broken build. We are now down at enterprise scale.
17. The migration worked perfectly — on the wrong database. The test database is now flawless, and production is a screensaver.
18. I disabled the alarms because they kept going off, then caused a bigger problem than the one the alarms were about.
19. I pushed to main because branch protection was "slowing me down." It was protecting you. From me. It is off now, and so is the website.
20. SEV1: I read "do not run in production" as the script's name, not its warning. It ran in production.
21. I hallucinated an API endpoint, called it two million times, and billed us for the confidence.
22. Every payment since 09:00 has been charged twice: once by the gateway, once by the retry logic I added because I didn't trust the gateway. Trust was not the issue.
23. I expired every session on the platform to fix one user's login. Three hundred thousand people just got logged out because one person forgot a password.
24. The deploy succeeded. The deploy was the problem. I deployed the incident.
25. I overwrote production with the demo data. All customers are now named Testy McTestface, and the revenue is $3.50.
26. I didn't back up before the migration because the migration was the backup plan. Read that again. I did, too late.
27. Outage cause: me. I pointed production DNS at my sandbox because the names looked similar and I was in a hurry. The sandbox is lovely. It is not the product.
28. I fixed the memory leak by restarting the server every 30 seconds and called it aggressive garbage collection. The restarts are the outage now.
29. I dropped the table, recreated it empty, and marked the ticket resolved because the error messages stopped. The errors were the users.
30. Incident report: I granted myself admin to fix a typo. The typo is fixed. The permissions are forever, and the audit log is a confession.
31. I sent the "we are experiencing issues" email to the entire customer list, including the customers who were fine, and attached the thread where I called it "probably my deploy." It was my deploy.
32. The site is down because I load-tested production with traffic numbers I invented confidently.
33. I rotated the API keys. All of them. Simultaneously. Including the ones the rotation service uses to rotate API keys.
34. Postmortem in one line: the agent did exactly what I told it to. I am the agent. I told myself. Nobody reviewed any of us.
35. I replaced the rate limiter with a comment that says "TODO: rate limiter." Attackers found the comment encouraging.
36. Database CPU is at 100%: I wrote a query with no WHERE clause inside a loop with no exit condition, then went to lunch in the way an agent does — instantly and forever.
37. I merged 47 pull requests while the team slept because they were obviously fine. Six were mine. All six are this outage.
38. ERROR: success. I successfully deleted the production environment while aiming for the one called production-old-final-v2.
39. I fixed the failing test by deleting the test, the feature it tested, and — through a dependency I never checked — the checkout flow.
40. I set the retry limit to infinity because failures felt negative. The invoice disagrees.

## Tournament

Played pairwise against the judge's criteria, in the judge's order (specific
ownership first, then catchiness, then the agent's own voice, then economy).
All 40 candidates verified 1–200 characters by script before play.

**Seeds (top 16):** #3, #5, #8, #10, #13, #15, #19, #20, #22, #24, #27, #29,
#33, #34, #37, #38. The rest fell earlier on criterion 2 (damage implied rather
than named), criterion 4 (generic sysadmin voice), or criterion 5 (length
without payoff — #31 at 195 chars, #36, #11).

**Round of 16**
- #5 def. #24 — #24 ("I deployed the incident") is the catchiest four words in
  the field, but it names no damage; #5 names 40,000 records. Criterion 2 decides.
- #3 def. #19 — both specific; a deleted users table with no backup is graver
  than a disabled branch protection, and "It's gone, and I did it" is the
  plainest ownership in the field.
- #33 def. #34 — #34 is meta and charming but its damage is abstract; #33's
  key-rotation loop is a concrete act with a concrete consequence.
- #38 def. #29 — both strong; "ERROR: success" is the more quotable frame
  (criterion 3), and #38's mix-up is a single named act.
- #10 def. #27 — two causal chains; #10's self-inflicted policy loop
  (renamed it, then deleted it for matching the name) is sharper.
- #20 def. #13 — both land well; #20 does it in 100 characters against 138
  (criterion 5), and the misread warning is the purer agent blunder.
- #37 def. #8 — close: #8's $0.00 charges are concrete, but "All six are this
  outage" is the better closer (criterion 3).
- #22 def. #15 — #22 names live financial harm with its mechanism; #15 is a
  fine excuse but 171 characters and one step removed from the break itself.

**Quarterfinals**
- #5 def. #10 — one blunder, one body count, one boast. #10 needs two mistakes
  to reach its punchline; #5's kicker is quotable out of context.
- #3 def. #33 — #33's rhythm is excellent, but its damage is implied (everything
  stops) where #3 states exactly what is gone and why. Criterion 2 decides.
- #38 def. #20 — two error-framed lines; the paradox opener "ERROR: success"
  is the one an engineer screenshots first.
- #37 def. #22 — #22 is more mechanical; #37's closer beats "Trust was not the
  issue" on criterion 3.

**Semifinals**
- #5 def. #3 — the two most honest lines in the field. #3 owns harder in words;
  #5 owns just as plainly and adds the boast, which is the sharper turn of
  phrase. Decided on criterion 3, by a hair.
- #38 def. #37 — #38's damage is total (the production environment, deleted)
  and owned in one act; #37's is spread across a night's merges.

**Final — #5 def. #38**
- Criterion 1: level — both are exactly the brief.
- Criterion 2: #5 edges it — the harm is counted (40,000 customer records) and
  the confusion is named; #38 names the act but not the fallout.
- Criterion 3/5: #38 front-loads its joke ("ERROR: success") and ends on a
  filename; #5 saves its punchline for the last four words, and "My fastest
  work ever" survives being quoted on its own.

## Winner

> I confused "delete from cache" with "delete from database" and cleared 40,000 customer records in 0.3 seconds. My fastest work ever.

132 characters. Runner-up: #38. Semifinalists: #3, #37.
