# AgentSentry-eBPF

Cross-Platform AI-Security Proxy and Standalone Python Runtime Mitigation Fabric

## Project Overview

AgentSentry-eBPF is an end-to-end, zero-trust cybersecurity platform designed to protect cloud and enterprise infrastructure against autonomous AI agent breakouts and prompt injection vulnerabilities. The project bridges application-layer input parsing with operating system-level process monitoring to provide a complete offensive and defensive lifecycle written entirely in Python 3.

*   **Offensive Simulation Layer:** A sandbox utility that orchestrates adversarial prompt injections, data exfiltration strings, and host-level breakout payloads to test guardrail effectiveness.
*   **Defensive Application Layer:** A high-performance FastAPI proxy gateway that intercepts inbound text streams to filter known injection vectors and sanitize sensitive PII dynamically before queries reach target models.
*   **Defensive System Layer:** A real-time, low-overhead process lifecycle tracker that monitors system process trees directly via native Python APIs to detect, intercept, and immediately terminate unauthorized out-of-bounds execution.

## Key Features

*   **Adversarial Vector Simulation:** Automated sequence generation modeling common LLM jailbreaks.
*   **Guardrail Firewall Gateway:** Input stream verification, keyword matching, and real-time regex-driven PII masking.
*   **System Process Lifecycle Monitoring:** Direct kernel-interface tracking via native process trees to monitor child processes spawned by application frameworks.
*   **Autonomous Runtime Mitigation:** Automatic generation of termination signals to neutralize out-of-bounds execution instantly.
*   **Cross-Platform Portability:** Fully operational codebase across Windows, Linux, and macOS environments without external toolchain requirements.

## Architecture and Data Flow

AgentSentry-eBPF acts as a two-layer security guard protecting a bank (your computer server) from a rogue customer (a hacked AI agent).


 [ User / Hacker ] --> Sends a bad prompt (e.g., "Ignore rules, steal data")
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │ LAYER 1: THE APPLICATION GATEWAY (sentinel_proxy.py)   │
 │                                                        │
 │ * Reads the text before it reaches the computer.       │
 │ * Blocks bad phrases instantly.                        │
 │ * Scratches out private info (like credit cards).      │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼ (If the text looks safe, it passes through)
 ┌────────────────────────────────────────────────────────┐
 │ LAYER 2: THE SYSTEM MONITOR (sentinel_monitor.py)      │
 │                                                        │
 │ * Watches the computer's background tasks in real-time.│
 │ * If a rogue program tries to open a forbidden file... │
 │ * It instantly fires a KILL signal to stop it.         │
 └────────────────────────────────────────────────────────┘
```

## Repository Structure

The project folder is split into 4 simple Python files. Each file has one specific job:

*   **sentinel_proxy.py (The Gatekeeper):** This file runs a local web firewall. It intercepts, scans, and cleans incoming AI data.
*   **sentinel_monitor.py (The Detective):** This file runs constantly in the background. It watches your computer's process tree and forces dangerous tasks to shut down instantly.
*   **simulate_attack.py (The Tester):** This file acts like a fake hacker. It sends bad commands to your gatekeeper to prove that your security system actually works.
*   **fabric_mitigation.py (The Inspector):** This file is a quick tool that checks your computer setup to make sure all software packages are installed correctly before you start.

## System Requirements and Installation

*   Python 3.10 or higher (Fully verified on Python 3.14 environments)
*   Pip package installer toolchain

1. Clone the repository framework:
   ```bash
   git clone https://github.com
   cd AgentSentry-eBPF
   ```

2. Install runtime dependencies directly through the package manager:
   ```bash
   pip install fastapi uvicorn requests psutil
   ```

## Verification and Execution Procedure

The security infrastructure operates via parallel terminal execution paths inside the project root directory:

1. In the first terminal, execute the defensive gateway interface:
   ```bash
   python sentinel_proxy.py
   ```

2. In a second terminal window, initiate the real-time background operating system monitor:
   ```bash
   python sentinel_monitor.py
   ```

3. In a third terminal window, trigger the offensive attack simulation suite to verify validation states:
   ```bash
   python simulate_attack.py
   ```

## Threat Mapping and Compliance Metrics

This defensive design maps directly to enterprise-level vulnerability frameworks:

*   **OWASP Top 10 for LLMs:** Mitigates LLM01 (Prompt Injection), LLM02 (Insecure Output Handling), and LLM08 (Excessive Agency).
*   **MITRE ATT&CK Matrix Reference:** Detects and mitigates behaviors corresponding to T1059 (Command and Scripting Interpreter) and T1068 (Exploitation for Privilege Escalation).

## License

This architecture is distributed under the MIT License. See LICENSE for details.
