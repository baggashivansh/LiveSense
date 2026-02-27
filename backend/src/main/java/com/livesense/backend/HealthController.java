package com.livesense.backend;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HealthController {

    @GetMapping("/")
    public String home() {
        return "LiveSense Backend is running 🚀";
    }

    @GetMapping("/health")
    public String health() {
        return "OK";
    }
}