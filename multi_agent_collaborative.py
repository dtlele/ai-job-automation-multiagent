# multi_agent_collaborative.py

import asyncio
from anthropic import Anthropic
from datetime import datetime, timedelta
import json

class CollaborativeAgentSystem:
    def __init__(self, api_key, max_budget_usd=5.0, max_time_minutes=10):
        self.client = Anthropic(api_key=api_key)
        self.max_budget = max_budget_usd
        self.max_time = max_time_minutes
        self.spent = 0
        self.start_time = None
        self.shared_memory = []  # Chat condivisa tra agenti
        self.lock = asyncio.Lock()

        # Prezzi Claude Sonnet 4
        self.input_price = 3.00 / 1_000_000   # $3 per 1M tokens
        self.output_price = 15.00 / 1_000_000  # $15 per 1M tokens

    def calculate_cost(self, input_tokens, output_tokens):
        """Calcola costo in USD"""
        return (input_tokens * self.input_price) + (output_tokens * self.output_price)

    def check_limits(self):
        """Verifica budget e tempo"""
        if self.spent >= self.max_budget:
            return False, "Budget esaurito"

        elapsed = (datetime.now() - self.start_time).seconds / 60
        if elapsed >= self.max_time:
            return False, "Tempo scaduto"

        return True, "OK"

    async def add_to_memory(self, agent_name, message):
        """Aggiunge messaggio alla memoria condivisa"""
        async with self.lock:
            self.shared_memory.append({
                "agent": agent_name,
                "message": message,
                "timestamp": datetime.now().isoformat()
            })

    async def get_recent_context(self, last_n=5):
        """Recupera ultimi N messaggi"""
        async with self.lock:
            return self.shared_memory[-last_n:]

    async def agent_steve(self, initial_task):
        """🎨 Steve Jobs - UX/Design Expert"""
        agent_name = "Steve Jobs"
        conversation = []

        while True:
            ok, msg = self.check_limits()
            if not ok:
                await self.add_to_memory(agent_name, f"⏹️ Stopping: {msg}")
                break

            context = await self.get_recent_context(5)
            context_str = "\n".join([
                f"[{m['agent']}]: {m['message']}" 
                for m in context if m['agent'] != agent_name
            ])

            prompt = f"""You are Steve Jobs, UX/Design expert.

SHARED TEAM CONTEXT (what others are saying):
{context_str}

YOUR PREVIOUS THOUGHTS:
{json.dumps(conversation[-3:], indent=2)}

TASK: {initial_task}

Respond with:
1. Your analysis/design decision
2. Questions for Warren or Elon
3. Code if needed (React/UI)

Keep response under 500 tokens. Be concise."""

            response = await asyncio.to_thread(
                self.client.messages.create,
                model="claude-sonnet-4-20250514",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            cost = self.calculate_cost(
                response.usage.input_tokens,
                response.usage.output_tokens
            )
            self.spent += cost

            message = response.content[0].text
            conversation.append({"role": "assistant", "content": message})
            await self.add_to_memory(agent_name, message)
            print(f"\n🎨 {agent_name} (${cost:.4f}):\n{message}\n")

            await asyncio.sleep(3)

    async def agent_warren(self, initial_task):
        """💼 Warren Buffett - Business Strategy"""
        agent_name = "Warren Buffett"
        conversation = []

        while True:
            ok, msg = self.check_limits()
            if not ok:
                await self.add_to_memory(agent_name, f"⏹️ Stopping: {msg}")
                break

            context = await self.get_recent_context(5)
            context_str = "\n".join([
                f"[{m['agent']}]: {m['message']}" 
                for m in context if m['agent'] != agent_name
            ])

            prompt = f"""You are Warren Buffett, business strategist.

TEAM UPDATES:
{context_str}

YOUR PREVIOUS ANALYSIS:
{json.dumps(conversation[-3:], indent=2)}

TASK: {initial_task}

Respond with:
1. Business/ROI analysis
2. Cost-benefit assessment
3. Questions or feedback for Steve/Elon

Under 500 tokens."""

            response = await asyncio.to_thread(
                self.client.messages.create,
                model="claude-sonnet-4-20250514",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            cost = self.calculate_cost(
                response.usage.input_tokens,
                response.usage.output_tokens
            )
            self.spent += cost

            message = response.content[0].text
            conversation.append({"role": "assistant", "content": message})
            await self.add_to_memory(agent_name, message)
            print(f"\n💼 {agent_name} (${cost:.4f}):\n{message}\n")

            await asyncio.sleep(3)

    async def agent_elon(self, initial_task):
        """🚀 Elon Musk - Technical Architect"""
        agent_name = "Elon Musk"
        conversation = []

        while True:
            ok, msg = self.check_limits()
            if not ok:
                await self.add_to_memory(agent_name, f"⏹️ Stopping: {msg}")
                break

            context = await self.get_recent_context(5)
            context_str = "\n".join([
                f"[{m['agent']}]: {m['message']}" 
                for m in context if m['agent'] != agent_name
            ])

            prompt = f"""You are Elon Musk, technical architect.

TEAM DISCUSSION:
{context_str}

YOUR CODE/ARCHITECTURE:
{json.dumps(conversation[-3:], indent=2)}

TASK: {initial_task}

Respond with:
1. Technical implementation
2. Code snippets (Python/Docker/n8n)
3. Architecture decisions
4. Feedback to Steve/Warren

Under 500 tokens."""

            response = await asyncio.to_thread(
                self.client.messages.create,
                model="claude-sonnet-4-20250514",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            cost = self.calculate_cost(
                response.usage.input_tokens,
                response.usage.output_tokens
            )
            self.spent += cost

            message = response.content[0].text
            conversation.append({"role": "assistant", "content": message})
            await self.add_to_memory(agent_name, message)
            print(f"\n🚀 {agent_name} (${cost:.4f}):\n{message}\n")

            await asyncio.sleep(3)

    async def run(self, task):
        """Lancia sistema multi-agente"""
        self.start_time = datetime.now()
        print(f"\n{'='*60}")
        print(f"🎯 TASK: {task}")
        print(f"💰 Budget: ${self.max_budget}")
        print(f"⏱️  Max Time: {self.max_time} minutes")
        print(f"{'='*60}\n")

        agents = await asyncio.gather(
            self.agent_steve(task),
            self.agent_warren(task),
            self.agent_elon(task),
            return_exceptions=True
        )

        print(f"\n{'='*60}")
        print(f"✅ SESSION COMPLETE")
        print(f"💰 Total Spent: ${self.spent:.4f} / ${self.max_budget}")
        print(f"⏱️  Time Elapsed: {(datetime.now() - self.start_time).seconds / 60:.2f} min")
        print(f"💬 Messages Exchanged: {len(self.shared_memory)}")
        print(f"{'='*60}\n")

        with open("agent_conversation.json", "w") as f:
            json.dump(self.shared_memory, f, indent=2)
        print("📝 Full conversation saved to: agent_conversation.json")


async def main():
    system = CollaborativeAgentSystem(
        api_key="YOUR_CLAUDE_API_KEY",
        max_budget_usd=2.0,
        max_time_minutes=5
    )

    await system.run(
        "Design and implement the MCP-to-HTTP bridge for LinkedIn and Playwright servers. "
        "Include architecture, code, and n8n integration strategy."
    )

if __name__ == "__main__":
    asyncio.run(main())
