# Beginners Guide Reorganization Design

## Overview
The goal of this project is to reorganize the "Beginners Guide" section of the EzBitcoin book to provide a more logical, "shallow to deep" learning path. Additionally, we will fix formatting and logical issues in the chapters to ensure a smooth reading experience.

## 1. Table of Contents Reorganization (`docs/index.md`)

The Beginners Guide will be restructured into distinct, logical phases:

**Phase 1: Introduction & Core Concepts**
* 新手导读及概览 (Beginners Intro)
* 比特币是如何工作的？ (How does Bitcoin work?)

**Phase 2: Acquisition (Getting Bitcoin)**
* 如何选择交易平台 (Exchanges)

**Phase 3: Storage & Safety**
* 如何选择钱包 (Wallets)
* 安全与存储防范 (Security)

**Phase 4: Usage**
* 如何发送与接收比特币 (Sending)

**Phase 5: Technical Primer**
* 新手极简图解手册 (Beginners Short Guide) - *All existing sub-items remain intact.*

## 2. Formatting & Logic Fixes

We will scan and update the markdown files in `docs/beginners/` focusing on the following:

* **Markdown Formatting**: 
  * Fix misaligned tables.
  * Ensure image links are correct and render properly.
  * Correct heading hierarchies (H1, H2, H3).
  * Fix any broken bold/italic syntax.
* **Logic/Flow Fixes**: 
  * Ensure the narrative flows logically according to the new structure. For example, the content should assume the user learns how to *buy* Bitcoin (Exchanges) before they learn how to *store* it (Wallets).
  * Fix any logical inconsistencies or contradictory statements found within the beginner chapters.
* **Conciseness**: 
  * Review the text to ensure descriptions are concise, clear, and easy to understand for beginners.

## 3. Implementation Plan Scope
This design is focused entirely on the Beginners Guide section. The Technical Guide and External Articles sections will remain untouched for this phase.
