# LiveSense

LiveSense is a real time Vision AI agent built for the Vision AI Hackathon.
The goal of this project is to explore how AI systems can observe live video, understand context, and generate meaningful responses with low latency.

This project focuses on system design, realtime processing, and practical multimodal AI integration rather than just running a demo.

## Hackathon Context

This project is being built as part of the Vision AI Hackathon by WeMakeDevs.

Hackathon link
[https://www.wemakedevs.org/hackathons/vision](https://www.wemakedevs.org/hackathons/vision)

## Core Idea

Most AI applications work with static inputs such as text or images.
LiveSense experiments with continuous video input where context evolves constantly.

The system captures live camera frames, processes them using vision models, reasons over context using an AI agent, and produces realtime responses.

## Architecture Overview

LiveSense follows a layered backend style architecture.

Input Layer
Handles camera capture and frame throttling to balance performance and accuracy.

Vision Processing Layer
Processes frames using vision models to extract structured visual context.

Agent Layer
Uses Vision Agents SDK to combine visual understanding with reasoning logic.

Output Layer
Generates responses that can be text based, spoken, or visual overlays.

Control Layer
Manages configuration, latency tuning, logging, and debugging.

## Tech Stack

Python
Vision Agents SDK
Realtime camera streaming
Vision models for frame understanding
Optional speech processing support

## Inspiration and Attribution

This project was inspired by realtime webcam vision demos such as:

https://github.com/ngxson/smolvlm-realtime-webcam

LiveSense is a ground up reimplementation focused on architecture clarity, Vision Agents integration, and hackathon specific experimentation.

## What Is Different Here

Clear backend oriented architecture instead of a single demo script
Integration with Vision Agents ecosystem
Focus on realtime system constraints such as latency and context continuity
Experimentation toward practical use cases instead of only visual demos

## Current Status

Active development during the hackathon.
Architecture evolving with ongoing experimentation and performance tuning.

## Future Scope

Realtime scene understanding assistants
Security and monitoring applications
Accessibility tools
Interactive AI overlays for live environments

## Author

Shivansh Bagga
