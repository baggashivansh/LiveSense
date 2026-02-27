package com.livesense.backend;

import org.springframework.web.bind.annotation.*;
import java.time.Instant;
import java.util.List;

@RestController
@RequestMapping("/vision")
@CrossOrigin(origins = "*")
public class VisionEventController {

    private final VisionEventRepository repository;

    public VisionEventController(VisionEventRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/events")
    public List<VisionEvent> getEvents() {
        return repository.findAll();
    }

    @PostMapping("/events")
    public VisionEvent addEvent(@RequestBody VisionEvent event) {
        event.setTimestamp(Instant.now());
        return repository.save(event);
    }
}