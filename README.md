# Prototype

> The agent replaces this heading with the prototype's name once the idea is clear.

## So funktioniert's

1. Arbeitsplatz öffnen. Die App läuft bereits unter **http://localhost:8000**. Anmelden heißt hier: eine Beispielperson auswählen.
2. Claude öffnen und schreiben, was du brauchst. Zum Beispiel: „Ich brauche ein Tool, um Ersatzteil-Rücksendungen zu erfassen.“
3. Fragen beantworten, eine nach der anderen. Nach wenigen Minuten steht die erste Version, und Claude sagt dir, wo du klicken sollst.
4. Weiterschreiben: Änderungswünsche, Feedback von Kolleginnen und Kollegen, eine Excel-Liste, ein Screenshot. Dateien kommen in den Ordner **inbox** oder direkt in den Chat.
5. Wenn es passt: „Wir sind fertig“ schreiben. Claude erstellt die Übergabe an die IT und gibt dir den Link.

Du musst nichts installieren, nichts starten und keine Datei bearbeiten. Es werden nur Beispieldaten verwendet, keine echten Personen- oder Kundendaten.

## How it works

1. Open the workspace. The app is already running at **http://localhost:8000**. Signing in means picking a sample person.
2. Open Claude and type what you need. For example: "I need a tool to record spare-part returns."
3. Answer the questions, one at a time. After a few minutes the first version is there and Claude tells you where to click.
4. Keep typing: change requests, feedback from colleagues, an Excel list, a screenshot. Files go into the **inbox** folder or straight into the chat.
5. When it fits, type "we are done". Claude prepares the handover to IT and gives you the link.

You do not install, start or edit anything. Only sample data is used, never real personal or customer data.

---

## About this prototype

*Maintained by the agent, in English. This section, `doc/code-map.md` and the `doc/memory-*.md` files are the handover to IT.*

| Passport | |
|---|---|
| **Name** | *(not set)* |
| **Department** | *(not set)* |
| **Owner** | *(not set)* |
| **Started** | *(not set)* |
| **Status** | new |
| **Target template** | Next.js Fullstack Template (Variant A) |

Status values: `new`, `building`, `validating`, then `validated`, `rejected` or `parked`, finally `handed-over`.

### Problem
*What is hard or slow today, and for whom?*

### Users and roles
*Who will use it, in which roles?*

### Today
*How is it done today: Excel, e-mail, paper, phone, another system?*

### Idea
*What the prototype does, in three to five sentences.*

### Expected benefit and how we measure it
*Example: "Technicians save 10 minutes per return. We compare the time for 10 returns before and after."*

### Out of scope
*What the prototype deliberately does not do.*

### Open questions
- *(none)*

### Result so far
*Feedback from test users about the value of the idea, not about colors and layout.*

### Result
*Filled at handover: tested with whom, did the expected benefit show, what the owner wants in the real app, what turned out unnecessary.*

### Needs for the real app
*Everything the prototype simulates or skips and the real application must do properly.*

| Need | In the prototype | In the real app |
|---|---|---|
| Login and roles | Fake login with sample persons, roles `ADMIN` and `USER` | Microsoft Entra ID, roles to be defined |
| Outbound messages | Simulated outbox page, nothing is sent | *(e-mail, Teams or other, to be defined)* |
