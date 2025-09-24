# Climapulse Python Developer Task

This repository contains my solution to a Python/Django coding task for Climapulse, focused on debugging a refrigerant withdrawal simulation and improving the overall user experience.

The task revolves around a simulation of withdrawals from a refrigerant vessel, where the vessel initially contains **50 Kg** of refrigerant. The simulation is designed to handle multiple users withdrawing from the vessel simultaneously. However, during testing, two major issues were identified:

1. **Lost Update Bug (Concurrency Issue):**  
   When two users attempted to withdraw 10 Kg each at the same time, only one withdrawal was applied. As a result, the vessel content decreased by 10 Kg instead of the expected 20 Kg.

2. **User Experience Problem with Empty Vessel:**  
   Users were able to attempt withdrawals even when the vessel was empty or had insufficient content. While the database prevented negative values, this triggered low-level exceptions rather than providing a clear, user-friendly message. This made the application prone to crashes or confusing error messages for end users.

The main objective of this task was to **identify and fix the lost update bug**, ensuring that concurrent withdrawals are accurately recorded, and to **enhance the user experience** by providing clear feedback when a withdrawal cannot be performed.


