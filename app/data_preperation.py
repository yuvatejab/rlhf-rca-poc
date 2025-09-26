import random
import json
import hashlib

# Expanded lists
events = [
    "API latency spike",
    "database connection failure",
    "user login outage",
    "payment processing error",
    "unexpected application crash",
    "security breach attempt",
    "network packet loss",
    "hardware disk failure",
    "memory exhaustion alert",
    "third-party service timeout",
    "DNS resolution failure",
    "container restart loop",
    "thread deadlock",
    "cache eviction storm",
    "disk full error",
    "configuration drift",
    "resource quota breach",
    "service coupling failure",
    "dependency version mismatch",
    "SSL / TLS handshake failure",
    "DNS amplification attack",
    "throttling due to rate limit",
    "circuit breaker open",
    "retry storm",
    "disk I/O saturation",
    "cache inconsistency",
    "leader election failure",
    "queue backlog overload",
    "overloaded thread pool",
    "excess GC pause time",
    "data serialization error",
    "invalid configuration state",
    "authentication token expiry",
    "API contract violation",
    "bad request flooding",
    "SSL certificate rotation failure",
    "latency tail-outlier",
    "log ingestion failure",
]


services = [
    "authentication service",
    "caching layer",
    "primary database",
    "billing API",
    "message queue",
    "load balancer",
    "payment gateway",
    "logging service",
    "search index",
    "file storage cluster",
    "DNS server",
    "Kubernetes control plane",
    "API gateway",
    "authorization service",
    "user profile service",
    "notification service",
    "email delivery service",
    "analytics pipeline",
    "metrics collector",
    "monitoring agent",
    "alerting service",
    "event bus",
    "stream processor",
    "data ingestion service",
    "data warehouse",
    "ETL job",
    "cache invalidation service",
    "session store",
    "session management",
    "configuration service",
    "feature flag service",
    "rate limiter",
    "circuit breaker",
    "service registry",
    "discovery service",
    "scheduler",
    "cron job runner",
    "background worker",
    "cron scheduler",
    "real-time processor",
    "batch processor",
    "analytics API",
    "reporting service",
    "tracing service",
    "distributed tracing",
    "correlation service",
    "gateway proxy",
    "reverse proxy",
    "edge service",
    "CDN",
    "cache cluster",
    "persistent queue",
    "notification queue",
    "web socket service",
    "socket server",
    "cache fallback service",
    "fallback endpoint",
    "fallback handler",
    "shutdown handler",
    "graceful shutdown service",
    "degradation service",
    "circuit breaker service"
]

issues = [
"an expired SSL certificate", "a memory leak", "a firewall misconfiguration",
"a faulty code deployment", "insufficient resource allocation",
"a dependency failure", "human error during configuration",
"a hardware wear-out issue", "a missing environment variable",
"an unhandled exception", "a DDoS attack", "a race condition in the code",
"database connection timeout", "disk space exhaustion", "CPU throttling",
"network packet loss", "DNS resolution failure", "load balancer misconfiguration",
"cache invalidation issue", "service discovery failure", "API rate limiting exceeded",
"thread pool exhaustion", "deadlock in database", "connection pool saturation",
"garbage collection pressure", "buffer overflow", "null pointer exception",
"timeout in external service call", "authentication token expiration",
"database index corruption", "file system corruption", "power supply failure",
"cooling system malfunction", "network switch failure", "router misconfiguration",
"VPN tunnel disconnection", "certificate chain validation error",
"outdated software version", "incompatible library versions", "missing security patches",
"configuration drift", "backup system failure", "monitoring blind spot",
"log rotation issue", "permission denied error", "resource contention",
"synchronization failure", "cluster split-brain", "consensus algorithm failure",
"message queue overflow", "event processing delay", "data serialization error",
"schema migration failure", "replication lag", "sharding imbalance",
"container orchestration failure", "image registry unavailable", "network policy violation",
"storage volume full", "I/O performance degradation", "kernel panic",
"application crash", "service mesh configuration error", "ingress controller failure",
"secret management system outage", "third-party service degradation",
"CDN cache miss storm", "websocket connection drop", "session store corruption",
"cross-origin resource sharing violation", "SQL injection vulnerability exploit",
"buffer underrun", "stack overflow", "heap corruption", "infinite loop condition",
"concurrency control failure", "distributed lock timeout", "eventual consistency lag",
"circuit breaker activation", "bulkhead pattern failure", "retry storm",
"cascading failure propagation", "upstream dependency timeout",
"downstream service unavailability", "inter-service communication failure",
"data pipeline stall", "ETL job failure", "batch processing timeout",
"real-time stream processing lag", "event ordering violation", "duplicate message processing",
"network partition", "Byzantine fault", "quorum loss", "leader election failure",
"gossip protocol disruption", "consensus timeout", "transaction rollback cascade",
"isolation level violation", "dirty read occurrence", "phantom read detection",
"serialization anomaly", "checkpoint failure", "write-ahead log corruption",
"storage engine crash", "table lock escalation", "index fragmentation",
"query optimizer regression", "execution plan degradation", "temporary table overflow",
"connection leak", "prepared statement cache overflow", "result set memory exhaustion",
"transaction log full", "tempdb space exhaustion", "statistics out of date",
"plan cache eviction", "lock wait timeout", "blocking chain formation"
]

actions = [
    "restarting the pods", "rolling back the deployment", "issuing a hotfix",
    "renewing the certificate", "replacing the faulty hardware",
    "patching the vulnerability", "scaling up resources",
    "correcting the configuration", "adding input validation",
    "enhancing monitoring and alerts", "improving documentation",
    "conducting a post-mortem review", "implementing circuit breakers",
    "updating security patches", "reconfiguring load balancers",
    "redeploying the service", "clearing cache memory",
    "rotating access keys", "updating DNS records",
    "adjusting firewall rules", "optimizing database queries",
    "increasing timeout values", "implementing rate limiting",
    "upgrading system dependencies", "fixing memory leaks",
    "resolving network connectivity issues", "updating container images",
    "implementing graceful shutdowns", "adding health checks",
    "configuring auto-scaling policies", "implementing retry mechanisms",
    "updating configuration files", "restarting affected services",
    "applying security updates", "implementing backup procedures",
    "configuring disaster recovery", "updating access permissions",
    "implementing logging improvements", "adding error handling",
    "configuring monitoring thresholds", "implementing failover mechanisms",
    "updating environment variables", "fixing database constraints",
    "implementing connection pooling", "updating API endpoints",
    "configuring SSL certificates", "implementing data validation",
    "updating cron job schedules", "fixing race conditions",
    "implementing caching strategies", "updating third-party integrations",
    "configuring resource limits", "implementing queue processing",
    "updating database indexes", "fixing authentication issues",
    "implementing throttling mechanisms", "updating deployment scripts",
    "configuring backup schedules", "implementing audit logging",
    "updating security policies", "fixing synchronization issues",
    "implementing health monitoring", "updating load balancing rules",
    "configuring session management", "implementing data encryption",
    "updating API rate limits", "fixing deadlock conditions",
    "implementing cleanup procedures", "updating monitoring dashboards",
    "configuring alert escalation", "implementing rollback procedures",
    "updating infrastructure templates", "fixing concurrency issues",
    "implementing performance tuning", "updating access control lists",
    "configuring network policies", "implementing data archiving",
    "updating service mesh configuration", "fixing resource contention",
    "implementing automated testing", "updating incident runbooks",
    "configuring compliance checks", "implementing chaos engineering",
    "updating container orchestration", "fixing startup dependencies",
    "implementing progressive deployment", "updating service discovery",
    "configuring traffic routing", "implementing observability tools",
    "updating maintenance windows", "fixing integration endpoints"
]


prompt_templates = [
    "Provide a Root Cause Analysis for the recent {event}.",
    "Summarize the RCA for the {event}.",
    "Explain the cause of the {event}.",
    "Analyze the root cause of the {event}.",
    "Document the RCA for the {event}.",
    "What caused the {event}?",
    "What went wrong with the {event}?",
    "Why did the {event} happen?",
    "Can you break down what caused the {event}?",
    "Help me understand the {event}.",
    "What's the story behind the {event}?",
    "Walk me through the {event}.",
    "What led to the {event}?",
    "How did the {event} occur?",
    "What was behind the {event}?",
    "Tell me about the {event}.",
    "What triggered the {event}?",
    "Give me the details on the {event}.",
    "What happened with the {event}?",
    "Explain what went down during the {event}.",
    "What was the root issue with the {event}?",
    "Why did we have the {event}?",
    "What's the full picture of the {event}?",
    "Can you investigate the {event}?",
    "What were the factors that caused the {event}?",
    "Break down the {event} for me.",
    "What's the real reason for the {event}?",
    "How do we explain the {event}?",
    "What was the underlying cause of the {event}?",
    "Give me a rundown of the {event}.",
    "What's the bottom line on the {event}?",
    "Why exactly did the {event} occur?",
    "What were the contributing factors to the {event}?",
    "Can you dig into what caused the {event}?",
    "What's the main reason behind the {event}?",
    "How did we end up with the {event}?",
    "What was the source of the {event}?",
    "Tell me why the {event} happened.",
    "What's the deal with the {event}?",
    "Can you trace back the {event}?",
    "What went sideways during the {event}?",
    "Why did things go wrong with the {event}?",
    "What was the chain of events for the {event}?",
    "How did the {event} come about?",
    "What's the backstory on the {event}?",
    "Can you get to the bottom of the {event}?",
    "What was the real problem with the {event}?",
    "Why are we dealing with the {event}?",
    "What set off the {event}?",
    "Can you piece together what happened with the {event}?"
]


chosen_templates = [
    "The root cause of the {event} was {issue} in the {service}. It was resolved by {action}.",
    "Investigation confirmed that the {event} originated from {issue} affecting the {service}. The problem was fixed by {action}.",
    "After analysis, the {event} was traced to {issue} within the {service}. Resolution was achieved through {action}.",
    "The {event} occurred due to {issue} in the {service}. The team mitigated it by {action}, and preventive measures were introduced.",
    "Root cause analysis showed that {issue} in the {service} triggered the {event}. The team addressed this by {action} and strengthened monitoring.",
    "We identified that {issue} in the {service} caused the {event}. The issue was fixed by {action}.",
    "The {event} happened because of {issue} in the {service}. We resolved it by {action}.",
    "Analysis revealed {issue} in the {service} led to the {event}. The team corrected this by {action}.",
    "Our investigation found that {issue} in the {service} was behind the {event}. We fixed it by {action}.",
    "The {event} was caused by {issue} in the {service}. Resolution involved {action}.",
    "We determined that {issue} in the {service} triggered the {event}. The problem was solved by {action}.",
    "The underlying cause of the {event} was {issue} in the {service}. We addressed it by {action}.",
    "Root cause identified: {issue} in the {service} led to the {event}. Fixed by {action}.",
    "Investigation showed {issue} in the {service} caused the {event}. Resolved through {action}.",
    "The {event} stemmed from {issue} in the {service}. We remediated by {action}.",
    "Analysis confirmed {issue} in the {service} was responsible for the {event}. Corrected by {action}.",
    "We traced the {event} back to {issue} in the {service}. The team resolved it by {action}.",
    "The {event} resulted from {issue} in the {service}. We implemented {action} to fix it.",
    "Our findings show {issue} in the {service} caused the {event}. Solution was {action}.",
    "The primary cause of the {event} was {issue} in the {service}. We fixed this by {action}.",
    "Investigation revealed that {issue} in the {service} was the source of the {event}. Resolved by {action}.",
    "The {event} was triggered by {issue} in the {service}. We corrected this through {action}.",
    "Root cause: {issue} in the {service} led to the {event}. Fixed via {action}.",
    "We found {issue} in the {service} caused the {event}. The issue was addressed by {action}.",
    "The {event} occurred because {issue} in the {service}. Resolution completed by {action}.",
    "Analysis indicated {issue} in the {service} was behind the {event}. Remediated by {action}.",
    "The source of the {event} was {issue} in the {service}. We resolved this by {action}.",
    "Investigation confirmed {issue} in the {service} triggered the {event}. Fixed by implementing {action}.",
    "The {event} was due to {issue} in the {service}. Problem solved by {action}.",
    "We identified {issue} in the {service} as the cause of the {event}. Corrective action: {action}."
]


rejected_templates = [
    "The cause of the {event} is unclear. It might be related to the {service}, but no definite conclusion was reached.",
    "The investigation into the {event} was inconclusive. The {service} may have been involved, but no resolution was applied.",
    "The {event} could not be traced to a specific cause. Some evidence points to the {service}, but it remains speculative.",
    "The {event} has no confirmed root cause. Although the {service} was reviewed, no corrective steps were taken.",
    "The exact reason for the {event} is unknown. The {service} is a possible factor, but nothing was verified.",
    "We're not sure what caused the {event}. The {service} might be involved, but we can't say for certain.",
    "The {event} happened, but we couldn't figure out why. There's some indication it's related to the {service}, but it's hard to tell.",
    "We looked into the {event} but didn't find anything definitive. The {service} could be a factor, though we're not really sure.",
    "It's unclear what led to the {event}. We suspect the {service} had something to do with it, but we couldn't prove it.",
    "The {event} remains a mystery. The {service} seems like it might be connected, but we don't have enough evidence.",
    "We investigated the {event} but came up empty. The {service} is possibly involved, but the findings are inconclusive.",
    "The root cause of the {event} couldn't be determined. The {service} appears to be related somehow, but it's just speculation.",
    "We're still unsure about what triggered the {event}. The {service} might have played a role, but we can't confirm it.",
    "The {event} investigation didn't yield clear results. There's a chance the {service} was involved, but we're not certain.",
    "We can't pinpoint what caused the {event}. The {service} is a potential culprit, but the evidence is weak.",
    "The {event} analysis was incomplete. The {service} could be responsible, but we didn't have enough time to investigate properly.",
    "We're stumped by the {event}. The {service} might be to blame, but we couldn't gather sufficient proof.",
    "The {event} cause is ambiguous. While the {service} seems suspicious, we weren't able to establish a clear connection.",
    "We investigated the {event} but hit a dead end. The {service} is possibly at fault, though we can't be sure.",
    "The {event} origin is uncertain. There are hints that the {service} was involved, but nothing concrete.",
    "We don't have a clear answer for the {event}. The {service} may have contributed, but the investigation was inconclusive.",
    "The {event} remains unexplained. The {service} appears to be linked somehow, but we lack definitive evidence.",
    "We couldn't get to the bottom of the {event}. The {service} seems relevant, but we're missing key information.",
    "The {event} cause is still unknown. The {service} might be connected, but our findings were inconclusive.",
    "We investigated the {event} but didn't reach any solid conclusions. The {service} could be involved, though it's uncertain.",
    "The {event} analysis yielded mixed results. The {service} appears to be a factor, but we can't say for sure.",
    "We're not confident about what caused the {event}. The {service} seems like a possibility, but the data is unclear.",
    "The {event} investigation was frustrating. We think the {service} might be related, but we couldn't prove anything.",
    "We looked at the {event} from multiple angles but still don't know. The {service} could be involved, but it's just a guess.",
    "The {event} remains unresolved. There's some indication the {service} played a part, but we lack solid evidence."
]


def generate_rca_pair():
   
    event = random.choice(events)
    service = random.choice(services)
    issue = random.choice(issues)
    action = random.choice(actions)

    prompt = random.choice(prompt_templates).format(event=event)
    chosen = random.choice(chosen_templates).format(event=event, service=service, issue=issue, action=action)
    rejected = random.choice(rejected_templates).format(event=event, service=service, issue=issue, action=action)

    return {"prompt": prompt, "chosen": chosen, "rejected": rejected}

def generate_unique_dataset(n_samples):
    
    
    dataset = []
    seen = set()

    while len(dataset) < n_samples:
        example = generate_rca_pair()
        example_str = json.dumps(example, sort_keys=True)
        hash_val = hashlib.md5(example_str.encode()).hexdigest()
        if hash_val not in seen:
            seen.add(hash_val)
            dataset.append(example)
    return dataset


if __name__ == "__main__":
    dataset = generate_unique_dataset(20)
    print(json.dumps(dataset, indent=2))




# import random



# events = ["API latency spike", "database connection failure", "user login outage", "payment processing error"]
# services = ["authentication service", "caching layer", "primary database", "billing API"]
# issues = ["a memory leak", "a misconfiguration in the firewall", "an expired SSL certificate", "a bug in the new deployment"]
# actions = ["restarting the pods", "rolling back the deployment", "issuing a hotfix", "renewing the certificate"]

# def generate_rca_pair():
    
   
#     event = random.choice(events)
#     service = random.choice(services)
#     issue = random.choice(issues)
#     action = random.choice(actions)
    
#     prompt = f"Provide a Root Cause Analysis for the recent {event}."
    
#     chosen = f"The root cause of the {event} was conclusively identified as {issue} in the {service}. The issue has been resolved by {action}."
    
#     rejected = f"It is unclear what caused the {event}. There might be a possible issue with the {service}, but the investigation was inconclusive."
    
#     return {"prompt": prompt, 
#             "chosen": chosen, 
#             "rejected": rejected}



        #   --------------------------------------------------------------------------------------------------------------------------


# import random
# import json
# import hashlib


# events = [
#     "API latency spike",
#     "database connection failure",
#     "user login outage",
#     "payment processing error",
#     "unexpected application crash",
#     "security breach attempt",
#     "network packet loss",
#     "hardware disk failure",
#     "memory exhaustion alert",
#     "third-party service timeout",
#     "DNS resolution failure",
#     "container restart loop",
#     "thread deadlock",
#     "cache eviction storm",
#     "disk full error",
#     "configuration drift",
#     "resource quota breach",
#     "service coupling failure",
#     "dependency version mismatch",
#     "SSL / TLS handshake failure",
#     "DNS amplification attack",
#     "throttling due to rate limit",
#     "circuit breaker open",
#     "retry storm",
#     "disk I/O saturation",
#     "cache inconsistency",
#     "leader election failure",
#     "queue backlog overload",
#     "overloaded thread pool",
#     "excess GC pause time",
#     "data serialization error",
#     "invalid configuration state",
#     "authentication token expiry",
#     "API contract violation",
#     "bad request flooding",
#     "SSL certificate rotation failure",
#     "latency tail-outlier",
#     "log ingestion failure",
# ]


# services = [
#     "authentication service",
#     "caching layer",
#     "primary database",
#     "billing API",
#     "message queue",
#     "load balancer",
#     "payment gateway",
#     "logging service",
#     "search index",
#     "file storage cluster",
#     "DNS server",
#     "Kubernetes control plane",
#     "API gateway",
#     "authorization service",
#     "user profile service",
#     "notification service",
#     "email delivery service",
#     "analytics pipeline",
#     "metrics collector",
#     "monitoring agent",
#     "alerting service",
#     "event bus",
#     "stream processor",
#     "data ingestion service",
#     "data warehouse",
#     "ETL job",
#     "cache invalidation service",
#     "session store",
#     "session management",
#     "configuration service",
#     "feature flag service",
#     "rate limiter",
#     "circuit breaker",
#     "service registry",
#     "discovery service",
#     "scheduler",
#     "cron job runner",
#     "background worker",
#     "cron scheduler",
#     "real-time processor",
#     "batch processor",
#     "analytics API",
#     "reporting service",
#     "tracing service",
#     "distributed tracing",
#     "correlation service",
#     "gateway proxy",
#     "reverse proxy",
#     "edge service",
#     "CDN",
#     "cache cluster",
#     "persistent queue",
#     "notification queue",
#     "web socket service",
#     "socket server",
#     "cache fallback service",
#     "fallback endpoint",
#     "fallback handler",
#     "shutdown handler",
#     "graceful shutdown service",
#     "degradation service",
#     "circuit breaker service"
# ]

# issues = [
# "an expired SSL certificate", "a memory leak", "a firewall misconfiguration",
# "a faulty code deployment", "insufficient resource allocation",
# "a dependency failure", "human error during configuration",
# "a hardware wear-out issue", "a missing environment variable",
# "an unhandled exception", "a DDoS attack", "a race condition in the code",
# "database connection timeout", "disk space exhaustion", "CPU throttling",
# "network packet loss", "DNS resolution failure", "load balancer misconfiguration",
# "cache invalidation issue", "service discovery failure", "API rate limiting exceeded",
# "thread pool exhaustion", "deadlock in database", "connection pool saturation",
# "garbage collection pressure", "buffer overflow", "null pointer exception",
# "timeout in external service call", "authentication token expiration",
# "database index corruption", "file system corruption", "power supply failure",
# "cooling system malfunction", "network switch failure", "router misconfiguration",
# "VPN tunnel disconnection", "certificate chain validation error",
# "outdated software version", "incompatible library versions", "missing security patches",
# "configuration drift", "backup system failure", "monitoring blind spot",
# "log rotation issue", "permission denied error", "resource contention",
# "synchronization failure", "cluster split-brain", "consensus algorithm failure",
# "message queue overflow", "event processing delay", "data serialization error",
# "schema migration failure", "replication lag", "sharding imbalance",
# "container orchestration failure", "image registry unavailable", "network policy violation",
# "storage volume full", "I/O performance degradation", "kernel panic",
# "application crash", "service mesh configuration error", "ingress controller failure",
# "secret management system outage", "third-party service degradation",
# "CDN cache miss storm", "websocket connection drop", "session store corruption",
# "cross-origin resource sharing violation", "SQL injection vulnerability exploit",
# "buffer underrun", "stack overflow", "heap corruption", "infinite loop condition",
# "concurrency control failure", "distributed lock timeout", "eventual consistency lag",
# "circuit breaker activation", "bulkhead pattern failure", "retry storm",
# "cascading failure propagation", "upstream dependency timeout",
# "downstream service unavailability", "inter-service communication failure",
# "data pipeline stall", "ETL job failure", "batch processing timeout",
# "real-time stream processing lag", "event ordering violation", "duplicate message processing",
# "network partition", "Byzantine fault", "quorum loss", "leader election failure",
# "gossip protocol disruption", "consensus timeout", "transaction rollback cascade",
# "isolation level violation", "dirty read occurrence", "phantom read detection",
# "serialization anomaly", "checkpoint failure", "write-ahead log corruption",
# "storage engine crash", "table lock escalation", "index fragmentation",
# "query optimizer regression", "execution plan degradation", "temporary table overflow",
# "connection leak", "prepared statement cache overflow", "result set memory exhaustion",
# "transaction log full", "tempdb space exhaustion", "statistics out of date",
# "plan cache eviction", "lock wait timeout", "blocking chain formation"
# ]

# actions = [
#     "restarting the pods", "rolling back the deployment", "issuing a hotfix",
#     "renewing the certificate", "replacing the faulty hardware",
#     "patching the vulnerability", "scaling up resources",
#     "correcting the configuration", "adding input validation",
#     "enhancing monitoring and alerts", "improving documentation",
#     "conducting a post-mortem review", "implementing circuit breakers",
#     "updating security patches", "reconfiguring load balancers",
#     "redeploying the service", "clearing cache memory",
#     "rotating access keys", "updating DNS records",
#     "adjusting firewall rules", "optimizing database queries",
#     "increasing timeout values", "implementing rate limiting",
#     "upgrading system dependencies", "fixing memory leaks",
#     "resolving network connectivity issues", "updating container images",
#     "implementing graceful shutdowns", "adding health checks",
#     "configuring auto-scaling policies", "implementing retry mechanisms",
#     "updating configuration files", "restarting affected services",
#     "applying security updates", "implementing backup procedures",
#     "configuring disaster recovery", "updating access permissions",
#     "implementing logging improvements", "adding error handling",
#     "configuring monitoring thresholds", "implementing failover mechanisms",
#     "updating environment variables", "fixing database constraints",
#     "implementing connection pooling", "updating API endpoints",
#     "configuring SSL certificates", "implementing data validation",
#     "updating cron job schedules", "fixing race conditions",
#     "implementing caching strategies", "updating third-party integrations",
#     "configuring resource limits", "implementing queue processing",
#     "updating database indexes", "fixing authentication issues",
#     "implementing throttling mechanisms", "updating deployment scripts",
#     "configuring backup schedules", "implementing audit logging",
#     "updating security policies", "fixing synchronization issues",
#     "implementing health monitoring", "updating load balancing rules",
#     "configuring session management", "implementing data encryption",
#     "updating API rate limits", "fixing deadlock conditions",
#     "implementing cleanup procedures", "updating monitoring dashboards",
#     "configuring alert escalation", "implementing rollback procedures",
#     "updating infrastructure templates", "fixing concurrency issues",
#     "implementing performance tuning", "updating access control lists",
#     "configuring network policies", "implementing data archiving",
#     "updating service mesh configuration", "fixing resource contention",
#     "implementing automated testing", "updating incident runbooks",
#     "configuring compliance checks", "implementing chaos engineering",
#     "updating container orchestration", "fixing startup dependencies",
#     "implementing progressive deployment", "updating service discovery",
#     "configuring traffic routing", "implementing observability tools",
#     "updating maintenance windows", "fixing integration endpoints"
# ]


# prompt_templates = [
#     "Provide a Root Cause Analysis for the recent {event}.",
#     "Summarize the RCA for the {event}.",
#     "Explain the cause of the {event}.",
#     "Analyze the root cause of the {event}.",
#     "Document the RCA for the {event}.",
#     "What caused the {event}?",
#     "What went wrong with the {event}?",
#     "Why did the {event} happen?",
#     "Can you break down what caused the {event}?",
#     "Help me understand the {event}.",
#     "What's the story behind the {event}?",
#     "Walk me through the {event}.",
#     "What led to the {event}?",
#     "How did the {event} occur?",
#     "What was behind the {event}?",
#     "Tell me about the {event}.",
#     "What triggered the {event}?",
#     "Give me the details on the {event}.",
#     "What happened with the {event}?",
#     "Explain what went down during the {event}.",
#     "What was the root issue with the {event}?",
#     "Why did we have the {event}?",
#     "What's the full picture of the {event}?",
#     "Can you investigate the {event}?",
#     "What were the factors that caused the {event}?",
#     "Break down the {event} for me.",
#     "What's the real reason for the {event}?",
#     "How do we explain the {event}?",
#     "What was the underlying cause of the {event}?",
#     "Give me a rundown of the {event}.",
#     "What's the bottom line on the {event}?",
#     "Why exactly did the {event} occur?",
#     "What were the contributing factors to the {event}?",
#     "Can you dig into what caused the {event}?",
#     "What's the main reason behind the {event}?",
#     "How did we end up with the {event}?",
#     "What was the source of the {event}?",
#     "Tell me why the {event} happened.",
#     "What's the deal with the {event}?",
#     "Can you trace back the {event}?",
#     "What went sideways during the {event}?",
#     "Why did things go wrong with the {event}?",
#     "What was the chain of events for the {event}?",
#     "How did the {event} come about?",
#     "What's the backstory on the {event}?",
#     "Can you get to the bottom of the {event}?",
#     "What was the real problem with the {event}?",
#     "Why are we dealing with the {event}?",
#     "What set off the {event}?",
#     "Can you piece together what happened with the {event}?"
# ]


# chosen_templates = [
#     "The root cause of the {event} was {issue} in the {service}. It was resolved by {action}.",
#     "Investigation confirmed that the {event} originated from {issue} affecting the {service}. The problem was fixed by {action}.",
#     "After analysis, the {event} was traced to {issue} within the {service}. Resolution was achieved through {action}.",
#     "The {event} occurred due to {issue} in the {service}. The team mitigated it by {action}, and preventive measures were introduced.",
#     "Root cause analysis showed that {issue} in the {service} triggered the {event}. The team addressed this by {action} and strengthened monitoring.",
#     "We identified that {issue} in the {service} caused the {event}. The issue was fixed by {action}.",
#     "The {event} happened because of {issue} in the {service}. We resolved it by {action}.",
#     "Analysis revealed {issue} in the {service} led to the {event}. The team corrected this by {action}.",
#     "Our investigation found that {issue} in the {service} was behind the {event}. We fixed it by {action}.",
#     "The {event} was caused by {issue} in the {service}. Resolution involved {action}.",
#     "We determined that {issue} in the {service} triggered the {event}. The problem was solved by {action}.",
#     "The underlying cause of the {event} was {issue} in the {service}. We addressed it by {action}.",
#     "Root cause identified: {issue} in the {service} led to the {event}. Fixed by {action}.",
#     "Investigation showed {issue} in the {service} caused the {event}. Resolved through {action}.",
#     "The {event} stemmed from {issue} in the {service}. We remediated by {action}.",
#     "Analysis confirmed {issue} in the {service} was responsible for the {event}. Corrected by {action}.",
#     "We traced the {event} back to {issue} in the {service}. The team resolved it by {action}.",
#     "The {event} resulted from {issue} in the {service}. We implemented {action} to fix it.",
#     "Our findings show {issue} in the {service} caused the {event}. Solution was {action}.",
#     "The primary cause of the {event} was {issue} in the {service}. We fixed this by {action}.",
#     "Investigation revealed that {issue} in the {service} was the source of the {event}. Resolved by {action}.",
#     "The {event} was triggered by {issue} in the {service}. We corrected this through {action}.",
#     "Root cause: {issue} in the {service} led to the {event}. Fixed via {action}.",
#     "We found {issue} in the {service} caused the {event}. The issue was addressed by {action}.",
#     "The {event} occurred because {issue} in the {service}. Resolution completed by {action}.",
#     "Analysis indicated {issue} in the {service} was behind the {event}. Remediated by {action}.",
#     "The source of the {event} was {issue} in the {service}. We resolved this by {action}.",
#     "Investigation confirmed {issue} in the {service} triggered the {event}. Fixed by implementing {action}.",
#     "The {event} was due to {issue} in the {service}. Problem solved by {action}.",
#     "We identified {issue} in the {service} as the cause of the {event}. Corrective action: {action}."
# ]


# rejected_templates = [
#     "The cause of the {event} is unclear. It might be related to the {service}, but no definite conclusion was reached.",
#     "The investigation into the {event} was inconclusive. The {service} may have been involved, but no resolution was applied.",
#     "The {event} could not be traced to a specific cause. Some evidence points to the {service}, but it remains speculative.",
#     "The {event} has no confirmed root cause. Although the {service} was reviewed, no corrective steps were taken.",
#     "The exact reason for the {event} is unknown. The {service} is a possible factor, but nothing was verified.",
#     "We're not sure what caused the {event}. The {service} might be involved, but we can't say for certain.",
#     "The {event} happened, but we couldn't figure out why. There's some indication it's related to the {service}, but it's hard to tell.",
#     "We looked into the {event} but didn't find anything definitive. The {service} could be a factor, though we're not really sure.",
#     "It's unclear what led to the {event}. We suspect the {service} had something to do with it, but we couldn't prove it.",
#     "The {event} remains a mystery. The {service} seems like it might be connected, but we don't have enough evidence.",
#     "We investigated the {event} but came up empty. The {service} is possibly involved, but the findings are inconclusive.",
#     "The root cause of the {event} couldn't be determined. The {service} appears to be related somehow, but it's just speculation.",
#     "We're still unsure about what triggered the {event}. The {service} might have played a role, but we can't confirm it.",
#     "The {event} investigation didn't yield clear results. There's a chance the {service} was involved, but we're not certain.",
#     "We can't pinpoint what caused the {event}. The {service} is a potential culprit, but the evidence is weak.",
#     "The {event} analysis was incomplete. The {service} could be responsible, but we didn't have enough time to investigate properly.",
#     "We're stumped by the {event}. The {service} might be to blame, but we couldn't gather sufficient proof.",
#     "The {event} cause is ambiguous. While the {service} seems suspicious, we weren't able to establish a clear connection.",
#     "We investigated the {event} but hit a dead end. The {service} is possibly at fault, though we can't be sure.",
#     "The {event} origin is uncertain. There are hints that the {service} was involved, but nothing concrete.",
#     "We don't have a clear answer for the {event}. The {service} may have contributed, but the investigation was inconclusive.",
#     "The {event} remains unexplained. The {service} appears to be linked somehow, but we lack definitive evidence.",
#     "We couldn't get to the bottom of the {event}. The {service} seems relevant, but we're missing key information.",
#     "The {event} cause is still unknown. The {service} might be connected, but our findings were inconclusive.",
#     "We investigated the {event} but didn't reach any solid conclusions. The {service} could be involved, though it's uncertain.",
#     "The {event} analysis yielded mixed results. The {service} appears to be a factor, but we can't say for sure.",
#     "We're not confident about what caused the {event}. The {service} seems like a possibility, but the data is unclear.",
#     "The {event} investigation was frustrating. We think the {service} might be related, but we couldn't prove anything.",
#     "We looked at the {event} from multiple angles but still don't know. The {service} could be involved, but it's just a guess.",
#     "The {event} remains unresolved. There's some indication the {service} played a part, but we lack solid evidence."
# ]




# def generate_rca_pair():
   
#     event = random.choice(events)
#     service = random.choice(services)
#     issue = random.choice(issues)
#     action = random.choice(actions)

#     prompt = random.choice(prompt_templates).format(event=event)
#     chosen = random.choice(chosen_templates).format(event=event, service=service, issue=issue, action=action)
#     rejected = random.choice(rejected_templates).format(event=event, service=service, issue=issue, action=action)

#     return {"prompt": prompt, "chosen": chosen, "rejected": rejected}


# def generate_unique_dataset(n_samples):
    
    
#     dataset = []
#     seen = set()

#     while len(dataset) < n_samples:
#         example = generate_rca_pair()
#         example_str = json.dumps(example, sort_keys=True)
#         hash_val = hashlib.md5(example_str.encode()).hexdigest()
#         if hash_val not in seen:
#             seen.add(hash_val)
#             dataset.append(example)
#     return dataset
