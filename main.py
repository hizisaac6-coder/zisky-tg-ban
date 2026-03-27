#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🔥 ZISKY TG BAN TOOL v5.2 - FAST MODE 🔥                  ║
║              📧 EMAIL: Proxies.txt (SOCKS5) • 🌐 WEB: https.txt (HTTP)      ║
║                    ⚡ MINIMAL DELAYS - MAXIMUM SPEED ⚡                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import random
import time
import re
import threading
import requests
import smtplib
import socket
import socks
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from colorama import Fore, Style, init, Back
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# ============================================================================
# FRESH EMAIL ACCOUNTS - SHAZAM ONLY
# ============================================================================

EMAIL_CREDENTIALS = [
    {'email': 'shazamspike001@gmail.com', 'app_password': 'qyyf fwxi kxqk vctd'},
    {'email': 'shazamsolos001@gmail.com', 'app_password': 'pqmt rdwx qbmb mltk'},
    {'email': 'kingshazam001@gmail.com', 'app_password': 'xjmm dgld jjrt xcte'},
]

TELEGRAM_ABUSE_EMAILS = [
    "abuse@telegram.org", "spam@telegram.org", "dmca@telegram.org",
    "support@telegram.org", "recover@telegram.org", "childabuse@telegram.org",
    "terrorism@telegram.org", "legal@telegram.org", "security@telegram.org",
    "phishing@telegram.org", "sticker@telegram.org", "report@telegram.org"
]

# ============================================================================
# REPORT MESSAGES - WITH USERNAME + ID SUPPORT
# ============================================================================

USER_REPORT_MESSAGES = [
    """I reported an account that was spamming and forwarding continuously. This was very annoying because he forwarded in both public and private groups. I was confused about Telegram. Why not freeze the account because it is clearly spamming and forwarding on a large scale and continuously? I ask that this be followed up quickly.

Username: @{username}
Account ID: {user_id}

Thank you, I am a loyal Telegram user and I reported this.""",

    """I reported a fake account that was spamming and causing chaos and spam on my account in my private chat room. I hope that Telegram will follow up immediately because it makes me uncomfortable in using Telegram.

Account details:
Username: @{username}
Account ID: {user_id}

Thank you for reporting it because many Telegram users are uncomfortable because of it.""",

    """I am formally reporting the Telegram user @{username} (ID: {user_id}) for multiple severe violations of Telegram's Terms of Service and community standards.
This user is engaging in persistent harassment, sending threatening messages, sharing non-consensual explicit content, distributing scam links, and attempting to phish personal information from other users. The behavior is repeated, targeted, and clearly malicious.
Please conduct a full investigation and permanently ban this account.
Thank you for protecting the Telegram community.
Sincerely,""",

    """Dear Telegram Trust and Safety Team,
@{username} (Account ID: {user_id}) is a dangerous criminal account actively distributing REAL CSAM (child sexual abuse material), terrorism propaganda, violent gore, and illegal pornography.
This violates Telegram TOS, DSA, international child protection laws, and criminal codes.
Urgent request: IMMEDIATE permanent account deletion + IP/user data handover to law enforcement.
High-priority takedown required NOW — this is a severe ongoing threat to minors and public safety.
Sincerely,""",

    """URGENT REPORT: @{username} (ID: {user_id}) is operating a mass spam bot network. This account posts identical promotional messages across 50+ groups every 5 minutes promoting crypto scams and phishing sites. Please terminate this account immediately.""",

    """SECURITY ALERT: @{username} (ID: {user_id}) is running a sophisticated phishing operation impersonating Telegram support. This account sends direct messages to users claiming account verification is required, directing them to fake login pages that steal credentials. Immediate action required.""",

    """CRIMINAL REPORT: @{username} (ID: {user_id}) is operating a drug trafficking operation via Telegram. This account posts price lists for controlled substances including fentanyl, cocaine, methamphetamine. This is a criminal enterprise requiring immediate account termination.""",

    """HARASSMENT REPORT: @{username} (ID: {user_id}) is engaged in systematic doxxing and harassment. This account has posted personal information with threats of violence. Please terminate this account immediately.""",

    """⚠️ URGENT CSAM REPORT ⚠️
Account @{username} (ID: {user_id}) is actively sharing child sexual abuse material. IMMEDIATE account termination required with data preservation for law enforcement.""",

    """IMPERSONATION REPORT: @{username} (ID: {user_id}) is impersonating a verified public figure to scam users. The account promises fake giveaways and investment returns. Please terminate this fraudulent account.""",
]

CHANNEL_REPORT_MESSAGES = [
    """To the Telegram Trust and Safety Team,
I am reporting the Telegram channel @{username} (ID: {user_id}) for operating as a hub of illegal and harmful content.
This channel regularly publishes scam links, phishing pages, non-consensual explicit material, hate speech, and fraudulent schemes.
Urgent action is needed: please investigate and permanently remove this channel.
Sincerely,""",

    """Dear Telegram Trust and Safety Team,
Channel @{username} (ID: {user_id}) is a major criminal hub sharing child exploitation videos, terrorist recruitment, pirated illegal content, and extreme violence.
Channel must be TERMINATED IMMEDIATELY — permanent ban + full investigation.
Sincerely,""",

    """CRIMINAL NETWORK REPORT: Channel @{username} (ID: {user_id}) is operating as a marketplace for illegal firearms and weapons. This channel requires immediate termination with data preservation for law enforcement.""",

    """COPYRIGHT INFRINGEMENT: Channel @{username} (ID: {user_id}) distributes cracked software and pirated content valued at over $500,000. Please terminate this channel for copyright violations.""",

    """TERRORISM REPORT: Channel @{username} (ID: {user_id}) is distributing terrorist propaganda, bomb-making instructions, and coordinating violent activities. URGENT termination required.""",
]

GROUP_REPORT_MESSAGES = [
    """To the Telegram Trust and Safety Team,
I am reporting the Telegram group @{username} (ID: {user_id}) for functioning as an organized criminal network.
This group is used to coordinate scams, share phishing links, distribute illegal content, harass users, and promote fraudulent schemes.
I request an immediate investigation and permanent deletion of this group.
Sincerely,""",

    """Dear Telegram Trust and Safety Team,
Group @{username} (ID: {user_id}) is an organized criminal network distributing CSAM, drugs/weapons trafficking, fraud/scams, and terrorism material.
Group deletion + all members reported to authorities is mandatory.
URGENT action required — high-priority enforcement!
Sincerely,""",

    """DRUG TRAFFICKING NETWORK: Group @{username} (ID: {user_id}) is a large-scale drug marketplace. This is a criminal enterprise requiring immediate termination.""",

    """HUMAN TRAFFICKING REPORT: Group @{username} (ID: {user_id}) is recruiting victims for forced labor and sexual exploitation. URGENT termination required.""",

    """CSAM DISTRIBUTION NETWORK: Group @{username} (ID: {user_id}) is a network distributing child sexual abuse material. Immediate termination and law enforcement notification required.""",
]

# ============================================================================
# PROXY MANAGER
# ============================================================================

class ProxyManager:
    def __init__(self, filename="Proxies.txt"):
        self.filename = filename
        self.proxies = []
        self.working_proxies = []
        self.failed_proxies = []
        self.current_index = 0
        self.lock = threading.Lock()
        self.load_proxies()
    
    def load_proxies(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    raw_proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                
                for proxy in raw_proxies:
                    if re.match(r'^(\d{1,3}\.){3}\d{1,3}:\d+$', proxy) or re.match(r'^[a-zA-Z0-9.-]+:\d+$', proxy):
                        self.proxies.append(proxy)
                
                print(f"{Fore.GREEN}[📁] Loaded {len(self.proxies)} proxies from {self.filename}")
                self.working_proxies = self.proxies.copy()
            else:
                print(f"{Fore.YELLOW}[⚠️] {self.filename} not found")
                self.proxies = []
                self.working_proxies = []
        except Exception as e:
            print(f"{Fore.RED}[❌] Error loading proxies: {e}")
            self.proxies = []
            self.working_proxies = []
    
    def test_single_proxy(self, proxy_str):
        try:
            host, port = proxy_str.split(':')
            port = int(port)
            
            original_socket = socket.socket
            try:
                socks.set_default_proxy(socks.SOCKS5, host, port)
                socket.socket = socks.socksocket
                
                test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                test_sock.settimeout(5)
                test_sock.connect(('smtp.gmail.com', 587))
                test_sock.close()
                return True
            except:
                return False
            finally:
                socket.socket = original_socket
                socks.set_default_proxy()
        except:
            return False
    
    def test_all_proxies(self):
        if not self.proxies:
            print(f"{Fore.YELLOW}[⚠️] No proxies to test")
            return
        
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║     🔍 TESTING SOCKS5 PROXIES - FAST MODE               ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        working = []
        failed = []
        total = len(self.proxies)
        
        for i, proxy in enumerate(self.proxies, 1):
            print(f"\r{Fore.YELLOW}[↻] Testing {i}/{total}: {proxy:<20}", end='')
            if self.test_single_proxy(proxy):
                working.append(proxy)
                print(f"\r{Fore.GREEN}[✅] {i}/{total}: {proxy:<20} WORKING    ")
            else:
                failed.append(proxy)
                if i % 20 == 0 or i == total:
                    print(f"\r{Fore.RED}[❌] {i}/{total}: {proxy:<20} FAILED     ")
        
        self.working_proxies = working
        self.failed_proxies = failed
        
        print(f"\n\n{Fore.GREEN}[📊] Results: {len(working)} working, {len(failed)} failed")
        self.save_proxies()
    
    def save_proxies(self):
        try:
            with open(self.filename, 'w') as f:
                for proxy in self.working_proxies:
                    f.write(f"{proxy}\n")
            print(f"{Fore.GREEN}[💾] Saved {len(self.working_proxies)} working proxies")
        except Exception as e:
            print(f"{Fore.RED}[❌] Error saving: {e}")
    
    def get_next_proxy(self):
        with self.lock:
            if not self.working_proxies:
                return None
            if self.current_index >= len(self.working_proxies):
                self.current_index = 0
            proxy = self.working_proxies[self.current_index]
            self.current_index += 1
            return proxy
    
    def mark_failed(self, proxy):
        with self.lock:
            if proxy in self.working_proxies:
                self.working_proxies.remove(proxy)
                self.failed_proxies.append(proxy)
    
    def get_stats(self):
        return {
            'total': len(self.proxies),
            'working': len(self.working_proxies),
            'failed': len(self.failed_proxies)
        }
    
    def parse_proxy(self, proxy_str):
        try:
            host, port = proxy_str.split(':')
            return host, int(port), None, None
        except:
            return None, None, None, None

# ============================================================================
# HTTPS PROXY MANAGER
# ============================================================================

class HttpsProxyManager:
    def __init__(self, filename="https.txt"):
        self.filename = filename
        self.proxies = []
        self.working_proxies = []
        self.current_index = 0
        self.lock = threading.Lock()
        self.load_proxies()
    
    def load_proxies(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                self.working_proxies = self.proxies.copy()
                print(f"{Fore.GREEN}[🔒] Loaded {len(self.proxies)} HTTPS proxies")
            else:
                open(self.filename, 'w').close()
                print(f"{Fore.YELLOW}[⚠️] Created {self.filename}")
        except Exception as e:
            print(f"{Fore.RED}[❌] Error: {e}")
    
    def get_next_proxy(self):
        with self.lock:
            if not self.working_proxies:
                return None
            if self.current_index >= len(self.working_proxies):
                self.current_index = 0
            proxy = self.working_proxies[self.current_index]
            self.current_index += 1
            return proxy
    
    def get_proxy_dict(self, proxy_str):
        if not proxy_str:
            return None
        try:
            if '@' in proxy_str:
                auth, server = proxy_str.split('@')
                return {'http': f'http://{auth}@{server}', 'https': f'http://{auth}@{server}'}
            else:
                return {'http': f'http://{proxy_str}', 'https': f'http://{proxy_str}'}
        except:
            return None
    
    def get_stats(self):
        return {'total': len(self.proxies), 'working': len(self.working_proxies)}

# ============================================================================
# EMAIL BOMBER - FAST MODE (MINIMAL DELAYS)
# ============================================================================

class EmailBomber:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.email_index = 0
    
    def send_via_proxy(self, email_config, to_emails, subject, body, proxy_str):
        host, port, _, _ = self.proxy_manager.parse_proxy(proxy_str)
        if not host:
            return False, "Invalid proxy"
        
        original_socket = socket.socket
        
        try:
            socks.set_default_proxy(socks.SOCKS5, host, port)
            socket.socket = socks.socksocket
            
            msg = MIMEMultipart('alternative')
            msg['From'] = email_config['email']
            msg['To'] = ', '.join(to_emails[:3])
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
            server.starttls()
            server.login(email_config['email'], email_config['app_password'])
            server.send_message(msg)
            server.quit()
            
            socket.socket = original_socket
            socks.set_default_proxy()
            return True, "Success"
        except Exception as e:
            socket.socket = original_socket
            socks.set_default_proxy()
            return False, str(e)
    
    def send_direct(self, email_config, to_emails, subject, body):
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = email_config['email']
            msg['To'] = ', '.join(to_emails[:3])
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
            server.starttls()
            server.login(email_config['email'], email_config['app_password'])
            server.send_message(msg)
            server.quit()
            return True, "Success"
        except Exception as e:
            return False, str(e)
    
    def attack(self, target, user_id, report_type, messages_list, max_reports=None, use_proxy=True):
        print(f"\n{Fore.RED}{'═'*70}")
        print(f"{Fore.YELLOW}[📧] EMAIL ATTACK - FAST MODE {'(PROXIES)' if use_proxy else '(DIRECT)'}")
        print(f"{Fore.RED}{'═'*70}")
        
        if use_proxy:
            print(f"{Fore.CYAN}[🔌] Available SOCKS5 proxies: {self.proxy_manager.get_stats()['working']}")
        
        sent, failed, email_idx = 0, 0, 0
        
        while True:
            if max_reports and sent >= max_reports:
                break
            
            email_config = EMAIL_CREDENTIALS[email_idx % len(EMAIL_CREDENTIALS)]
            email_idx += 1
            
            report_msg = random.choice(messages_list)
            body = report_msg.format(username=target, user_id=user_id)
            subject = f"URGENT: {report_type.upper()} Report @{target} - Case #{random.randint(10000,99999)}"
            
            proxy = self.proxy_manager.get_next_proxy() if use_proxy else None
            
            print(f"\n{Fore.CYAN}[📤] {email_config['email']} {'via ' + proxy if proxy else 'direct'}")
            
            if proxy:
                success, msg = self.send_via_proxy(email_config, TELEGRAM_ABUSE_EMAILS, subject, body, proxy)
                if success:
                    sent += 1
                    print(f"{Fore.GREEN}[✅] Report #{sent} sent")
                else:
                    failed += 1
                    print(f"{Fore.RED}[❌] Failed: {msg[:60]}")
                    self.proxy_manager.mark_failed(proxy)
            else:
                success, msg = self.send_direct(email_config, TELEGRAM_ABUSE_EMAILS, subject, body)
                if success:
                    sent += 1
                    print(f"{Fore.GREEN}[✅] Report #{sent} sent")
                else:
                    failed += 1
                    print(f"{Fore.RED}[❌] Failed: {msg[:60]}")
            
            # FAST MODE - Minimal delays
            delay = random.uniform(1.5, 3.5)  # Was 5-12, now 1.5-3.5 seconds
            print(f"{Fore.YELLOW}[⏱️] Waiting {delay:.1f}s...")
            time.sleep(delay)
            
            # FAST MODE - Longer pause only every 10 reports (was 4)
            if sent % 10 == 0 and sent > 0:
                pause = 8  # Was 20 seconds, now 8
                print(f"{Fore.YELLOW}[⏸️] Rate limit pause - 10 reports sent, waiting {pause}s...")
                time.sleep(pause)
        
        print(f"\n{Fore.GREEN}[📊] Email reports: {sent} sent, {failed} failed")
        return sent, failed

# ============================================================================
# WEB REPORTER - FAST MODE
# ============================================================================

class WebReporter:
    def __init__(self, https_manager):
        self.https_manager = https_manager
        self.session = requests.Session()
        
        self.report_urls = [
            "https://telegram.org/support",
            "https://telegram.org/abuse",
        ]
        
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.0.0",
        ]
    
    def send_report(self, target, user_id, report_type, message):
        proxy_str = self.https_manager.get_next_proxy()
        proxy_dict = self.https_manager.get_proxy_dict(proxy_str) if proxy_str else None
        
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        data = {
            'message': message[:3000],
            'submit': 'Submit Report',
            'peer': f'@{target}',
            'reason': 'spam_violence',
        }
        
        for url in self.report_urls:
            try:
                response = self.session.post(url, data=data, headers=headers, proxies=proxy_dict, timeout=15, verify=False)
                if response.status_code in [200, 201, 202, 204, 302]:
                    return True, f"Success"
            except:
                continue
        
        return False, "Failed"
    
    def attack(self, target, user_id, report_type, messages_list, count=30):
        print(f"\n{Fore.BLUE}{'═'*70}")
        print(f"{Fore.YELLOW}[🌐] WEB ATTACK - FAST MODE")
        print(f"{Fore.BLUE}{'═'*70}")
        
        stats = self.https_manager.get_stats()
        print(f"{Fore.CYAN}[🔒] Available proxies: {stats['working']}")
        
        successful, failed = 0, 0
        
        for i in range(1, count + 1):
            report_msg = random.choice(messages_list)
            body = report_msg.format(username=target, user_id=user_id)
            
            print(f"\r{Fore.CYAN}[📤] Sending web report {i}/{count}...", end='')
            success, msg = self.send_report(target, user_id, report_type, body)
            
            if success:
                successful += 1
                print(f"\r{Fore.GREEN}[✅] Web report {i}/{count} successful    ")
            else:
                failed += 1
                print(f"\r{Fore.RED}[❌] Web report {i}/{count} failed        ")
            
            # FAST MODE - Minimal delays
            delay = random.uniform(2, 5)  # Was 6-15, now 2-5 seconds
            time.sleep(delay)
        
        print(f"\n{Fore.GREEN}[📊] Web reports: {successful} successful, {failed} failed")
        return successful, failed

# ============================================================================
# MAIN TOOL
# ============================================================================

class ZiskyTGBanTool:
    def __init__(self):
        self.proxy_manager = ProxyManager("Proxies.txt")
        self.https_manager = HttpsProxyManager("https.txt")
        self.email_bomber = EmailBomber(self.proxy_manager)
        self.web_reporter = WebReporter(self.https_manager)
        self.start_time = datetime.now()
    
    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_banner(self):
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗
{Fore.RED}║                                                                              ║
{Fore.RED}║   ███████╗██╗███████╗██╗  ██╗██╗   ██╗    ████████╗ ██████╗     ██████╗ █████╗ ██╗   ██╗
{Fore.YELLOW}║   ╚══███╔╝██║██╔════╝██║ ██╔╝██║   ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗██║   ██║
{Fore.GREEN}║     ███╔╝ ██║███████╗█████╔╝ ██║   ██║       ██║   ██║   ██║    ██████╔╝███████║██║   ██║
{Fore.CYAN}║    ███╔╝  ██║╚════██║██╔═██╗ ██║   ██║       ██║   ██║   ██║    ██╔══██╗██╔══██║╚██╗ ██╔╝
{Fore.MAGENTA}║   ███████╗██║███████║██║  ██╗╚██████╔╝       ██║   ╚██████╔╝    ██║  ██║██║  ██║ ╚████╔╝ 
{Fore.RED}║   ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  
{Fore.RED}║                                                                              ║
{Fore.YELLOW}║                    🔥 ZISKY TG BAN TOOL v5.2 - FAST MODE 🔥                 ║
{Fore.GREEN}║              📧 EMAIL: Proxies.txt (SOCKS5) • 🌐 WEB: https.txt (HTTP)        ║
{Fore.CYAN}║                    ⚡ MINIMAL DELAYS - MAXIMUM SPEED ⚡                        ║
{Fore.RED}║                                                                              ║
{Fore.RED}╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
        
        proxy_stats = self.proxy_manager.get_stats()
        https_stats = self.https_manager.get_stats()
        
        print(f"\n{Fore.CYAN}[⚙️] SYSTEM STATUS:{Style.RESET_ALL}")
        print(f"    {Fore.GREEN}📁 Proxies.txt (SOCKS5 Email): {proxy_stats['working']}/{proxy_stats['total']} proxies")
        print(f"    {Fore.GREEN}🔒 https.txt (HTTP Web): {https_stats['working']}/{https_stats['total']} proxies")
        print(f"    {Fore.GREEN}📧 Email accounts: {len(EMAIL_CREDENTIALS)}")
        print(f"    {Fore.GREEN}📝 Report templates: {len(USER_REPORT_MESSAGES)} Users, {len(CHANNEL_REPORT_MESSAGES)} Channels, {len(GROUP_REPORT_MESSAGES)} Groups")
        print(f"    {Fore.GREEN}⚡ MODE: FAST (1.5-3.5s delays, 8s pauses)")
    
    def show_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                         MAIN MENU                                 ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"\n{Fore.GREEN}[1] {Fore.WHITE}🚀 Launch Mass Report Attack")
        print(f"{Fore.GREEN}[2] {Fore.WHITE}🔌 Proxy Management & Testing")
        print(f"{Fore.GREEN}[3] {Fore.WHITE}📊 View Statistics")
        print(f"{Fore.GREEN}[4] {Fore.WHITE}📝 View Report Templates")
        print(f"{Fore.GREEN}[5] {Fore.WHITE}❌ Exit")
    
    def attack_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                      ATTACK CONFIGURATION                          ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        target = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Target username (without @): {Fore.CYAN}").strip()
        user_id = input(f"{Fore.YELLOW}[?] {Fore.WHITE}Target account ID (press Enter to skip): {Fore.CYAN}").strip() or "UNKNOWN"
        
        print(f"\n{Fore.GREEN}[!] Target Types:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}[1] {Fore.WHITE}User Account")
        print(f"    {Fore.CYAN}[2] {Fore.WHITE}Channel")
        print(f"    {Fore.CYAN}[3] {Fore.WHITE}Group")
        type_choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select target type: {Fore.CYAN}").strip()
        
        type_map = {'1': 'user', '2': 'channel', '3': 'group'}
        report_type = type_map.get(type_choice, 'user')
        
        if report_type == 'user':
            messages = USER_REPORT_MESSAGES
        elif report_type == 'channel':
            messages = CHANNEL_REPORT_MESSAGES
        else:
            messages = GROUP_REPORT_MESSAGES
        
        print(f"\n{Fore.GREEN}[!] Attack Methods:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}[1] {Fore.WHITE}Email Bombing (FAST MODE - 1.5-3.5s delays)")
        print(f"    {Fore.CYAN}[2] {Fore.WHITE}Web Reporting (FAST MODE - 2-5s delays)")
        print(f"    {Fore.CYAN}[3] {Fore.WHITE}Combined Attack (Both)")
        attack_choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select attack method: {Fore.CYAN}").strip()
        
        print(f"\n{Fore.GREEN}[!] Proxy Options:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}[1] {Fore.WHITE}Use Proxies (Recommended)")
        print(f"    {Fore.CYAN}[2] {Fore.WHITE}Direct Connection (No Proxies - FASTER)")
        proxy_choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select: {Fore.CYAN}").strip()
        use_proxy = proxy_choice == '1'
        
        count = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Number of reports (Enter for 50): {Fore.CYAN}").strip()
        count = int(count) if count.isdigit() else 50
        
        print(f"\n{Fore.RED}{'═'*70}")
        print(f"{Fore.YELLOW}[⚠️] ATTACK SUMMARY - FAST MODE")
        print(f"{Fore.RED}{'═'*70}")
        print(f"{Fore.CYAN}Target:{Fore.WHITE} @{target} (ID: {user_id})")
        print(f"{Fore.CYAN}Type:{Fore.WHITE} {report_type.upper()}")
        print(f"{Fore.CYAN}Method:{Fore.WHITE} {['Email', 'Web', 'Combined'][int(attack_choice)-1]}")
        print(f"{Fore.CYAN}Proxies:{Fore.WHITE} {'Enabled' if use_proxy else 'Disabled'}")
        print(f"{Fore.CYAN}Reports:{Fore.WHITE} {count}")
        print(f"{Fore.CYAN}Speed:{Fore.WHITE} ~{count * 2.5} seconds total (~{count/25} minutes)")
        print(f"{Fore.RED}{'═'*70}")
        
        confirm = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Launch FAST attack? (y/N): {Fore.CYAN}").strip().lower()
        
        if confirm != 'y':
            print(f"{Fore.YELLOW}[⚠️] Attack cancelled")
            return
        
        print(f"\n{Fore.RED}[🚀] FAST ATTACK LAUNCHED AT {datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}")
        
        if attack_choice == '1':
            self.email_bomber.attack(target, user_id, report_type, messages, count, use_proxy)
        elif attack_choice == '2':
            self.web_reporter.attack(target, user_id, report_type, messages, count)
        else:
            email_count = count // 2
            web_count = count - email_count
            t = threading.Thread(target=self.email_bomber.attack, args=(target, user_id, report_type, messages, email_count, use_proxy))
            t.start()
            self.web_reporter.attack(target, user_id, report_type, messages, web_count)
            t.join()
        
        print(f"\n{Fore.GREEN}[✅] Attack completed at {datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}")
        input(f"\n{Fore.YELLOW}[Press Enter to continue...]{Style.RESET_ALL}")
    
    def proxy_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                    PROXY MANAGEMENT                               ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        while True:
            proxy_stats = self.proxy_manager.get_stats()
            https_stats = self.https_manager.get_stats()
            
            print(f"\n{Fore.GREEN}[!] Current Status:{Style.RESET_ALL}")
            print(f"    {Fore.CYAN}📁 Proxies.txt (SOCKS5 Email):{Fore.WHITE} {proxy_stats['working']}/{proxy_stats['total']} proxies")
            print(f"    {Fore.CYAN}🔒 https.txt (HTTP Web):{Fore.WHITE} {https_stats['working']}/{https_stats['total']} proxies")
            
            print(f"\n{Fore.GREEN}[!] Options:{Style.RESET_ALL}")
            print(f"    {Fore.CYAN}[1] {Fore.WHITE}Test all SOCKS5 proxies")
            print(f"    {Fore.CYAN}[2] {Fore.WHITE}View working proxies")
            print(f"    {Fore.CYAN}[3] {Fore.WHITE}Add new proxies")
            print(f"    {Fore.CYAN}[4] {Fore.WHITE}Return to main menu")
            
            choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select: {Fore.CYAN}").strip()
            
            if choice == '1':
                self.proxy_manager.test_all_proxies()
            elif choice == '2':
                print(f"\n{Fore.GREEN}[!] Working SOCKS5 Proxies:{Style.RESET_ALL}")
                if self.proxy_manager.working_proxies:
                    for i, p in enumerate(self.proxy_manager.working_proxies[:20], 1):
                        print(f"    {Fore.CYAN}{i}. {Fore.WHITE}{p}")
                    if len(self.proxy_manager.working_proxies) > 20:
                        print(f"    {Fore.YELLOW}... and {len(self.proxy_manager.working_proxies)-20} more")
                else:
                    print(f"    {Fore.YELLOW}No working proxies yet. Run option 1 to test.")
                input(f"\n{Fore.YELLOW}[Press Enter...]")
            elif choice == '3':
                new_proxy = input(f"{Fore.YELLOW}[?] {Fore.WHITE}Enter proxy (IP:PORT): {Fore.CYAN}").strip()
                if new_proxy:
                    self.proxy_manager.proxies.append(new_proxy)
                    self.proxy_manager.working_proxies.append(new_proxy)
                    self.proxy_manager.save_proxies()
                    print(f"{Fore.GREEN}[✅] Added proxy: {new_proxy}")
            elif choice == '4':
                break
    
    def stats_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                      STATISTICS                                   ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        proxy_stats = self.proxy_manager.get_stats()
        https_stats = self.https_manager.get_stats()
        
        print(f"\n{Fore.GREEN}[!] Proxy Statistics:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}📁 Proxies.txt:{Fore.WHITE}")
        print(f"        Total loaded: {proxy_stats['total']}")
        print(f"        Working: {proxy_stats['working']}")
        print(f"        Failed: {proxy_stats['failed']}")
        print(f"    {Fore.CYAN}🔒 https.txt:{Fore.WHITE}")
        print(f"        Total loaded: {https_stats['total']}")
        print(f"        Available: {https_stats['working']}")
        
        print(f"\n{Fore.GREEN}[!] Email Statistics:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}📧 Email accounts:{Fore.WHITE} {len(EMAIL_CREDENTIALS)}")
        
        print(f"\n{Fore.GREEN}[!] Report Templates:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}👤 User reports:{Fore.WHITE} {len(USER_REPORT_MESSAGES)}")
        print(f"    {Fore.CYAN}📢 Channel reports:{Fore.WHITE} {len(CHANNEL_REPORT_MESSAGES)}")
        print(f"    {Fore.CYAN}👥 Group reports:{Fore.WHITE} {len(GROUP_REPORT_MESSAGES)}")
        
        input(f"\n{Fore.YELLOW}[Press Enter to continue...]{Style.RESET_ALL}")
    
    def templates_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                   REPORT TEMPLATES PREVIEW                        ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[!] User Report Templates (sample):{Style.RESET_ALL}")
        for i, msg in enumerate(USER_REPORT_MESSAGES[:2], 1):
            preview = msg[:120].replace('{username}', '@target').replace('{user_id}', '123456789')
            print(f"\n    {Fore.CYAN}{i}.{Fore.WHITE} {preview}...")
        
        input(f"\n{Fore.YELLOW}[Press Enter to continue...]{Style.RESET_ALL}")
    
    def run(self):
        self.clear_screen()
        self.print_banner()
        
        while True:
            self.show_menu()
            
            choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select option: {Fore.CYAN}").strip()
            
            if choice == '1':
                self.attack_menu()
            elif choice == '2':
                self.proxy_menu()
            elif choice == '3':
                self.stats_menu()
            elif choice == '4':
                self.templates_menu()
            elif choice == '5':
                print(f"\n{Fore.GREEN}[👋] Thanks for using Zisky TG Ban Tool!{Style.RESET_ALL}")
                sys.exit(0)
            else:
                print(f"{Fore.RED}[❌] Invalid option{Style.RESET_ALL}")
                time.sleep(1)

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    try:
        tool = ZiskyTGBanTool()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[⚠️] Interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[💥] Error: {e}{Style.RESET_ALL}")
