# ✅ Real-time memory cache for BioLinkRemoverBot

# In-memory authorized users
# Format: { chat_id: [user_id1, user_id2, ...] }
auth_users = {}

# In-memory warn counts
# Format: { chat_id: { user_id: warn_count } }
warns = {}

# In-memory bioscan toggle state
# Format: { chat_id: True/False }
bioscan_enabled = {}

# In-memory approved (safe) users to skip scan/warn
# Format: { chat_id: [user_id1, user_id2, ...] }
approved_users = {}
