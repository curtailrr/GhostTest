# Replay Analysis Report

**Replay ID:** 62c3e543-4394-4eec-9dde-ff11f297d15a  
**Recording ID:** 96423cb6-3397-4249-b000-0010017fabac  
**Status:** Completed  
**Created:** 2026-02-09 07:28:00  
**Target:** https://104.155.183.28  
**Analysis Date:** 2026-02-09 19:30:52

---

## Executive Summary

This report provides a comprehensive analysis of the latest replay execution. The replay detected **1,444 deltas** across 75 endpoints when comparing the recording baseline against the target environment. The analysis includes performance metrics, delta distribution patterns, and semantic classifications to identify potential bugs, configuration differences, and version-related changes.

### Key Findings

- **Total Deltas:** 1,444 differences detected
- **Endpoints Analyzed:** 75 endpoints
- **Critical Issues:** Multiple high-severity deltas requiring investigation
- **Performance Impact:** Significant performance variations observed in several endpoints

---

## Delta Summary

### Overall Statistics

| Metric | Count |
|--------|-------|
| Total Deltas | 1,444 |
| Endpoints Affected | 75 |
| Status | 100% Automatically Classified |

### Severity Distribution

Based on the grouped results, the severity breakdown across major endpoint groups:

- **High Severity:** 19 deltas (schedules, tenant status, tenant details)
- **Medium Severity:** ~1,200 deltas (schedules, data sources, policies)
- **Low Severity:** ~225 deltas (collections, resources, trending data)

---

## Top Affected Endpoints

### 1. `/compliance/api/v2/schedules` - 874 Deltas
- **Severity:** Medium (874 deltas)
- **Impact:** High volume of deltas on compliance schedules endpoint
- **Recommendation:** Review compliance schedule data structure and synchronization

### 2. `/tpmhub-inventory/api/v1/dataSources` - 233 Deltas
- **Severity:** Medium (92), Low (141)
- **Impact:** Data source inventory differences
- **Recommendation:** Investigate data source configuration differences between environments

### 3. `/compliance/api/v2/guiTransform/policies` - 158 Deltas
- **Severity:** Medium (149), Low (9)
- **Impact:** Policy transformation differences
- **Recommendation:** Review policy configuration and transformation logic

### 4. `/entrust-tpm-aggregation-service/api/v1/vaultSummary` - 40 Deltas
- **Severity:** Medium (40)
- **Impact:** Vault summary data discrepancies
- **Recommendation:** Verify vault aggregation data consistency

### 5. `/tpmhub-inventory/api/v1/dataSources/:id` - 28 Deltas
- **Severity:** Medium (14), Low (14)
- **Impact:** Individual data source details differ
- **Recommendation:** Check data source ID mappings and metadata

---

## Performance Analysis

### Critical Performance Changes

The following endpoints show significant performance differences (>100ms change):

#### Slower in Replay

1. **`/api/licensing/v1/license/summary/`**
   - Recording: 295.4ms → Replay: 992.6ms
   - **Change:** +697.2ms (+236.1%)
   - **Confidence:** Very Low (n=1)
   - **Status:** ⚠️ Significant degradation

2. **`/compliance/api/v2/policies/categories`**
   - Recording: 161.1ms → Replay: 645.0ms
   - **Change:** +484.0ms (+300.5%)
   - **Confidence:** Very Low (n=1)
   - **Status:** ⚠️ Significant degradation

3. **`/entrust-tenant-service/api/v1/tenant/{id}`**
   - Recording: 165.8ms → Replay: 623.1ms
   - **Change:** +457.4ms (+275.9%)
   - **Confidence:** Very Low (n=1)
   - **Status:** ⚠️ Significant degradation

4. **`/entrust-tpm-aggregation-service/api/v1/vaultSummary`**
   - Recording: 150.6ms → Replay: 391.3ms
   - **Change:** +240.7ms (+159.8%)
   - **Confidence:** Low (n=4)
   - **Status:** ⚠️ Degradation

5. **`/tpmhub-inventory/api/v1/collections`**
   - Recording: 127.7ms → Replay: 353.0ms
   - **Change:** +225.3ms (+176.3%)
   - **Confidence:** Low (n=4)
   - **Status:** ⚠️ Degradation

#### Faster in Replay

1. **`/v5/appliance/info/`**
   - Recording: 1646.7ms → Replay: 921.8ms
   - **Change:** -724.8ms (-44.0%)
   - **Confidence:** Low (n=7)
   - **Status:** ✅ Improvement

2. **`/entrust-tenant-service/api/v1/tenant/smtpEnabled`**
   - Recording: 1074.3ms → Replay: 819.4ms
   - **Change:** -254.9ms (-23.7%)
   - **Confidence:** Low (n=5)
   - **Status:** ✅ Improvement

---

## Semantic Pattern Analysis

The semantic analysis identified 4 distinct pattern clusters covering all 1,444 deltas:

### Cluster 1: Numeric Pattern (199 deltas)
- **Type:** Numeric values
- **Action Required:** Review
- **Label:** `requires-review`
- **Confidence:** 90%
- **Analysis:** Numeric differences that may represent:
  - ID mismatches requiring ID mapping
  - Version numbers or counters
  - Timestamps (should be filtered as noise)
  - Pagination or offset values

### Cluster 2: Text Pattern (852 deltas)
- **Type:** Text content
- **Action Required:** Review
- **Label:** `content-change`
- **Confidence:** 90%
- **Analysis:** Text-based differences representing:
  - Content changes between versions
  - Configuration differences
  - Potentially legitimate data evolution
  - Possible string-based ID differences

### Cluster 3: Unknown Pattern (331 deltas)
- **Type:** Unknown/Mixed
- **Action Required:** Review
- **Label:** `requires-review`
- **Confidence:** 90%
- **Analysis:** Complex or mixed-type differences requiring:
  - Manual inspection to determine root cause
  - Possible structural changes
  - Edge cases or unusual data patterns

### Cluster 4: Structural Pattern (62 deltas)
- **Type:** Structural/Schema
- **Action Required:** Review
- **Label:** `requires-review`
- **Confidence:** 90%
- **Analysis:** Schema or structure changes indicating:
  - API schema evolution
  - Field additions/removals
  - Type mismatches
  - Data structure refactoring

---

## High-Priority Issues

### Schedule Configuration Issues
- **Endpoint:** `/compliance/api/v2/schedules/:id`
- **Delta Count:** 10
- **Severity:** High
- **Description:** High-severity deltas in compliance schedule configuration
- **Impact:** Critical for compliance operations
- **Next Steps:** Immediate investigation required

### Tenant Status Discrepancies
- **Endpoint:** `/entrust-tenant-service/api/v1/tenant/:id/status`
- **Delta Count:** 9
- **Severity:** High (3), Medium (3), Low (3)
- **Description:** Tenant status inconsistencies across environments
- **Impact:** May affect tenant management operations
- **Next Steps:** Verify tenant synchronization

### Tenant Details Mismatches
- **Endpoint:** `/entrust-tenant-service/api/v1/tenant/:id`
- **Delta Count:** 6
- **Severity:** High
- **Description:** Tenant detail differences
- **Impact:** Core tenant data inconsistencies
- **Next Steps:** Review tenant data integrity

---

## Recommendations

### Immediate Actions (High Priority)

1. **Investigate Schedule Configuration**
   - Review the 10 high-severity deltas in `/compliance/api/v2/schedules/:id`
   - Verify schedule configuration consistency
   - Check for missing or extra schedule entries

2. **Analyze Performance Degradations**
   - Investigate licensing endpoint performance (236% slower)
   - Review policy categories endpoint (300% slower)
   - Profile tenant service endpoints showing degradation

3. **Review High-Severity Tenant Issues**
   - Verify tenant status synchronization
   - Check tenant detail consistency
   - Ensure tenant data integrity

### Short-Term Actions

4. **Create Filter Rules for Noise Reduction**
   - Identify timestamp fields in numeric pattern cluster
   - Create DROP rules for ephemeral session data
   - Map ID fields that represent the same logical entities

5. **Investigate Bulk Schedule Deltas**
   - 874 medium-severity deltas in compliance schedules need review
   - Determine if these are legitimate configuration differences or bugs
   - Consider creating LABEL rules if these are expected environmental differences

6. **Review Data Source Inventory**
   - 233 deltas in data source inventory
   - Verify data source configuration across environments
   - Check for missing or extra data sources

### Long-Term Actions

7. **Establish Baseline Noise Reduction Profile**
   - Use semantic pattern analysis to identify common noise patterns
   - Create comprehensive filter rules profile
   - Apply profile retroactively to validate effectiveness

8. **Performance Monitoring**
   - Set up performance thresholds for critical endpoints
   - Monitor trends over multiple replays
   - Investigate root causes of significant performance changes

9. **Automated Delta Classification**
   - Label known-good differences (environment URLs, config)
   - Create mappings for ID fields
   - Reduce manual review burden for future replays

---

## Next Steps

### For Immediate Investigation

1. **Query specific delta details:**
   ```
   Use regrade-query_deltas with specific filters:
   - category: ["data", "headers", "status"]
   - delta_type: ["value_mismatch", "missing", "extra"]
   - severity: ["critical", "high"]
   - request_url_pattern: Target specific endpoints
   ```

2. **Get delta context for root cause analysis:**
   ```
   Use regrade-get_delta_request_context for specific delta IDs
   to see full request/response data from recording vs replay
   ```

3. **Batch update delta labels:**
   ```
   Use regrade-batch_update_deltas to mark deltas as:
   - 'bug-[name]' for root cause issues
   - 'side-effect-of-[bug-name]' for cascading deltas
   - 'environment-difference' for expected config differences
   - 'requires-mapping' for ID field mismatches
   ```

4. **Create noise reduction rules:**
   ```
   Use regrade-create_filter_rule to automate:
   - DROP rules for timestamps, sessions, ephemeral data
   - LABEL rules for known environment differences
   Use regrade-create_id_mapping for ID field mappings
   ```

### Performance Investigation

- Focus on endpoints with >200% performance degradation
- Review sample sizes and confidence levels
- Increase sample collection for low-confidence measurements
- Profile slow endpoints to identify bottlenecks

---

## Conclusion

The replay analysis reveals **1,444 deltas** across 75 endpoints, with the majority being medium-severity changes concentrated in compliance schedules (874 deltas) and data source inventory (233 deltas). 

**Critical attention needed:**
- High-severity issues in schedule configuration, tenant status, and tenant details
- Significant performance degradations in licensing, policy, and tenant service endpoints
- Large volume of medium-severity deltas requiring systematic review

**Success criteria for next replay:**
- Reduce delta count by 50% through noise filtering and ID mapping
- Resolve all high-severity deltas
- Improve performance on degraded endpoints
- Establish automated classification for known difference patterns

This analysis provides a foundation for targeted bug investigation and systematic noise reduction to improve future replay signal-to-noise ratio.
