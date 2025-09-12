 ┌───────────────────────────┐
 │   Start Program           │
 │   Print "WELCOME..."      │
 │   should_continue = True  │
 └───────────┬───────────────┘
             │
             ▼
 ┌───────────────────────────┐
 │ While should_continue:    │
 └───────────┬───────────────┘
             │
             ▼
 ┌───────────────────────────┐
 │ firstGo():                │
 │  - Deal 2 random cards to │
 │    player & computer      │
 │  - Replace Ace (11→1) if  │
 │    sum > 21               │
 │  - Show cards & scores    │
 └───────────┬───────────────┘
             │
             ▼
 ┌───────────────────────────┐
 │ Check Draw? (equal sums)  │───Yes──▶ Print "Draw" → check() → Restart
 └───────────┬───────────────┘
             │ No
             ▼
 ┌───────────────────────────┐
 │ Player Blackjack (21)?    │───Yes──▶ Print "You Won" → check()
 └───────────┬───────────────┘
             │ No
             ▼
 ┌───────────────────────────┐
 │ Computer Blackjack (21)?  │───Yes──▶ Print "Computer Won" → check()
 └───────────┬───────────────┘
             │ No
             ▼
 ┌───────────────────────────┐
 │ Computer Bust (>21)?      │───Yes──▶ Print "Computer Lost"
 └───────────┬───────────────┘
             │ No
             ▼
 ┌───────────────────────────┐
 │ Player Bust (>21)?        │───Yes──▶ Print "You Lose"
 └───────────┬───────────────┘
             │ No
             ▼
 ┌───────────────────────────┐
 │ checker()? ("y" to hit)   │
 └───────┬─────────┬─────────┘
         │Yes      │No
         ▼         ▼
 ┌───────────────────────────┐   ┌───────────────────────────┐
 │ Both draw 1 new card each │   │ computerSumCheckFor21():   │
 │ Show updated hands        │   │  - If dealer < 17, draw    │
 │ Compare sums:             │   │  - If >=21 → finalcheck    │
 │   - If equal → Draw       │   │  - Else → recurse check    │
 │   - Else → finalcheck()   │   └───────────────────────────┘
 └───────────────────────────┘
