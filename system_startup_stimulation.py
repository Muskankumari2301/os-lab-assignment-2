#!/usr/bin/env python3
"""
OS Lab Assignment 2: System Startup, Process Creation, and Termination Simulation
Course: ENCS351 Operating System
Student: [Your Name]
"""

import multiprocessing
import time
import logging
import random
import sys
from datetime import datetime

def setup_logging():
    """Sub-Task 1: Initialize logging configuration with timestamps and process names"""
    logging.basicConfig(
        filename='process_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(processName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # Also log to console for better visibility
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(processName)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)

def system_process(task_name, duration=2):
    """
    Sub-Task 2: Simulate a system process task
    Args:
        task_name: Name of the process
        duration: How long the process runs (seconds)
    """
    process_id = multiprocessing.current_process().name
    logging.info(f"🟢 {task_name} STARTED (PID: {process_id})")
    
    # Simulate different types of system processes
    if "Boot" in task_name:
        # Boot process simulation
        logging.info(f"🔧 {task_name}: Initializing hardware components...")
        time.sleep(duration * 0.3)
        logging.info(f"🔧 {task_name}: Loading kernel modules...")
        time.sleep(duration * 0.4)
        logging.info(f"🔧 {task_name}: Starting system services...")
        time.sleep(duration * 0.3)
    
    elif "Service" in task_name:
        # Service process simulation
        for i in range(3):
            logging.info(f"🛠️ {task_name}: Performing service task {i+1}/3")
            time.sleep(duration / 3)
    
    elif "User" in task_name:
        # User process simulation
        tasks = ["Loading user profile", "Starting applications", "Initializing desktop"]
        for task in tasks:
            logging.info(f"👤 {task_name}: {task}")
            time.sleep(duration / len(tasks))
    
    else:
        # Generic process - just sleep
        time.sleep(duration)
    
    logging.info(f"🔴 {task_name} COMPLETED (Runtime: {duration} seconds)")

def system_startup_sequence():
    """Simulate the complete system startup sequence"""
    logging.info("=" * 60)
    logging.info("🚀 SYSTEM STARTUP SEQUENCE INITIATED")
    logging.info("=" * 60)
    
    # Define different system processes
    processes_config = [
        {"name": "Boot-Loader", "duration": 3},
        {"name": "Kernel-Init", "duration": 2},
        {"name": "Service-Manager", "duration": 4},
        {"name": "Network-Service", "duration": 2},
        {"name": "User-Session", "duration": 3}
    ]
    
    processes = []
    
    # Create and start all processes
    for config in processes_config:
        process = multiprocessing.Process(
            target=system_process,
            args=(config["name"], config["duration"]),
            name=config["name"]
        )
        processes.append(process)
        process.start()
        logging.info(f"📋 Process {config['name']} LAUNCHED")
        time.sleep(0.5)  # Stagger process startup
    
    return processes

def monitor_system_status(processes):
    """Monitor the system processes and wait for completion"""
    logging.info("📊 SYSTEM STATUS: Monitoring active processes...")
    
    # Check process status periodically
    all_done = False
    while not all_done:
        active_count = sum(1 for p in processes if p.is_alive())
        logging.info(f"📊 SYSTEM STATUS: {active_count} processes still running")
        
        if active_count == 0:
            all_done = True
        else:
            time.sleep(1)
    
    logging.info("✅ All processes completed successfully")

def system_shutdown_sequence():
    """Simulate system shutdown sequence"""
    logging.info("=" * 60)
    logging.info("🛑 SYSTEM SHUTDOWN SEQUENCE INITIATED")
    logging.info("=" * 60)
    
    shutdown_tasks = [
        "Saving system state",
        "Stopping user services",
        "Terminating network connections",
        "Unloading kernel modules",
        "Powering down hardware"
    ]
    
    for task in shutdown_tasks:
        logging.info(f"🔴 SHUTDOWN: {task}")
        time.sleep(0.5)
    
    logging.info("✅ SYSTEM SHUTDOWN COMPLETED")

def main():
    """Main function to run the complete system simulation"""
    print("🎓 OS LAB ASSIGNMENT 2: SYSTEM STARTUP SIMULATION")
    print("=" * 60)
    
    # Setup logging
    setup_logging()
    
    try:
        # System Startup
        startup_time = datetime.now()
        logging.info(f"🕐 System boot started at: {startup_time}")
        
        # Start all processes
        processes = system_startup_sequence()
        
        # Monitor system
        monitor_system_status(processes)
        
        # Wait for all processes to complete
        for process in processes:
            process.join()
            logging.info(f"✓ Process {process.name} joined successfully")
        
        # System Shutdown
        system_shutdown_sequence()
        
        shutdown_time = datetime.now()
        total_runtime = (shutdown_time - startup_time).total_seconds()
        
        logging.info("=" * 60)
        logging.info(f"📈 SYSTEM BOOT SUMMARY")
        logging.info(f"🕐 Startup Time: {startup_time}")
        logging.info(f"🕐 Shutdown Time: {shutdown_time}")
        logging.info(f"⏱️  Total Runtime: {total_runtime:.2f} seconds")
        logging.info(f"📊 Processes Executed: {len(processes)}")
        logging.info("🎉 SYSTEM SIMULATION COMPLETED SUCCESSFULLY")
        logging.info("=" * 60)
        
    except Exception as e:
        logging.error(f"💥 SYSTEM ERROR: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
