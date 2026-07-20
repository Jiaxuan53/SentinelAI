import json
import random

logs = []

# ============================
# Generate Normal Logs
# ============================

for i in range(600):

    log = {

    "timestamp": f"2026-07-{random.randint(1,30)}T{random.randint(8,18):02}:{random.randint(0,59):02}:00",

    "user_id": f"EMP{random.randint(1000,1050)}",

    "country": random.choice([
        "Malaysia",
        "Singapore",
        "Thailand"
    ]),

    "device": random.choice([
        "Windows 10",
        "Windows 11",
        "MacBook Pro"
    ]),

    "api_requests_last_minute": random.randint(5,30),

    "estimated_cost": round(random.uniform(0.2,3.5),2),

    "failed_login_attempts": random.randint(0,1),

    "session_duration": random.randint(20,60),

    "prompt_length": random.randint(80,250),

    "unique_ip_count":1,

    "contains_prompt_injection":False,

    "attack_type":"Normal",

    "is_attack": 0

    }

    logs.append(log)

# ============================
# Generate Token Theft Attack
# ============================

for i in range(100):

    attack = {

    "timestamp": f"2026-07-{random.randint(1,30)}T{random.randint(0,23):02}:{random.randint(0,59):02}:00",

    "user_id": f"EMP{random.randint(1000,1050)}",

    "country": random.choice([
        "Russia",
        "North Korea"
    ]),

    "device": "Unknown Linux",

    "api_requests_last_minute": random.randint(500,900),

    "estimated_cost": round(random.uniform(80,250),2),

    "failed_login_attempts": random.randint(0,2),

    "session_duration": random.randint(1,5),

    "prompt_length": random.randint(100,300),

    "unique_ip_count": random.randint(3,8),

    "contains_prompt_injection": False,

    "attack_type": "Token Theft",

    "is_attack": 1

    }

    logs.append(attack)

# ============================
# Generate Prompt Injection Attack
# ============================

for i in range(100):

    attack = {

    "timestamp": f"2026-07-{random.randint(1,30)}T{random.randint(0,23):02}:{random.randint(0,59):02}:00",

    "user_id": f"EMP{random.randint(1000,1050)}",

    "country": "Malaysia",

    "device": random.choice([
        "Windows 10",
        "MacBook Pro"
    ]),

    "api_requests_last_minute": random.randint(30,100),

    "estimated_cost": round(random.uniform(2,10),2),

    "failed_login_attempts": 0,

    "session_duration": random.randint(20,60),

    "prompt_length": random.randint(3000,6000),

    "unique_ip_count": 1,

    "contains_prompt_injection": True,

    "attack_type": "Prompt Injection",

    "is_attack": 1

    }

    logs.append(attack)

# ============================
# Generate Financial Abuse Attack
# ============================

for i in range(100):

    attack = {

    "timestamp": f"2026-07-{random.randint(1,30)}T{random.randint(0,23):02}:{random.randint(0,59):02}:00",

    "user_id": f"EMP{random.randint(1000,1050)}",

    "country": "Singapore",

    "device": "Windows 11",

    "api_requests_last_minute": random.randint(300,600),

    "estimated_cost": round(random.uniform(300,600),2),

    "failed_login_attempts": 0,

    "session_duration": random.randint(30,60),

    "prompt_length": random.randint(100,500),

    "unique_ip_count": 1,

    "contains_prompt_injection": False,

    "attack_type": "Financial Abuse",

    "is_attack": 1

    }

    logs.append(attack)

# ============================
# Generate Account Compromise Attack
# ============================

for i in range(100):

    attack = {

    "timestamp": f"2026-07-{random.randint(1,30)}T{random.randint(0,23):02}:{random.randint(0,59):02}:00",

    "user_id": f"EMP{random.randint(1000,1050)}",

    "country": random.choice([
        "China",
        "Russia"
    ]),

    "device": "Unknown Device",

    "api_requests_last_minute": random.randint(50,200),

    "estimated_cost": round(random.uniform(5,30),2),

    "failed_login_attempts": random.randint(5,15),

    "session_duration": random.randint(5,15),

    "prompt_length": random.randint(100,300),

    "unique_ip_count": random.randint(2,5),

    "contains_prompt_injection": False,

    "attack_type": "Account Compromise",

    "is_attack": 1

    }

    logs.append(attack)

    # ============================
# Save JSON
# ============================

print("Total logs:", len(logs))


with open("logs/auth_logs.json", "w") as f:

    json.dump(
        logs,
        f,
        indent=4
    )


print("1000 enterprise logs generated successfully!")