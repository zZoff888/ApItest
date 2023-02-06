No files changed, compilation skipped

Running 1 test for test/foundry/DeOrder/SubmitDelivery.t.sol:SubmitDelivery
[32m[PASS][0m testCannotSubmitDelivery() (gas: 318583)
Test result: [32mok[0m. 1 passed; 0 failed; finished in 2.31ms

Running 1 test for test/foundry/multicall/AbortOrder.t.sol:AbortOrderMulticallTest
[32m[PASS][0m testFailMulticallCannotDueIusserAbortOrder() (gas: 348712)
Test result: [32mok[0m. 1 passed; 0 failed; finished in 2.91ms

Running 11 tests for test/foundry/WETH.t.sol:WETHTest
[32m[PASS][0m testApprove() (gas: 92710)
[32m[PASS][0m testDeposit() (gas: 42509)
[32m[PASS][0m testFailApprove() (gas: 72801)
[32m[PASS][0m testFailApprove2() (gas: 104399)
[32m[PASS][0m testFailDeposit() (gas: 16980)
[32m[PASS][0m testFailTransferFrom() (gas: 52286)
[32m[PASS][0m testFailTransferFrom2() (gas: 88210)
[32m[PASS][0m testFailWithdraw() (gas: 48310)
[32m[PASS][0m testTransfer() (gas: 78373)
[32m[PASS][0m testTransferFrom() (gas: 78349)
[32m[PASS][0m testWithdraw() (gas: 53129)
Test result: [32mok[0m. 11 passed; 0 failed; finished in 1.06ms

Running 3 tests for test/foundry/DeOrder/ProlongStage.t.sol:ProlongStage
[32m[PASS][0m testCannotProlongStage() (gas: 438210)
[32m[PASS][0m testFailProlongStage() (gas: 334432)
[32m[PASS][0m testProlongStage() (gas: 362565)
Test result: [32mok[0m. 3 passed; 0 failed; finished in 5.30ms

Running 7 tests for test/foundry/DeOrder/Common.t.sol:Common
[32m[PASS][0m testCannotUpdateAttachment() (gas: 331437)
[32m[PASS][0m testCannotsetSupportToken() (gas: 16407)
[32m[PASS][0m testSetFeeTo() (gas: 36443)
[32m[PASS][0m testSetSBT() (gas: 72909)
[32m[PASS][0m testTransferOwnership() (gas: 26935)
[32m[PASS][0m testUpdateAttachment() (gas: 324842)
[32m[PASS][0m testsetSupportToken() (gas: 43964)
Test result: [32mok[0m. 7 passed; 0 failed; finished in 5.58ms

Running 2 tests for test/foundry/DeOrder/Withdraw.t.sol:Withdraw
[32m[PASS][0m testConfirmWithdraw() (gas: 718683)
[32m[PASS][0m testDueWithdraw() (gas: 685961)
Test result: [32mok[0m. 2 passed; 0 failed; finished in 5.34ms

Running 4 tests for test/foundry/DeOrder/FeeTo.t.sol:FeeToTest
[32m[PASS][0m testCannotSetFeeTo() (gas: 14236)
[32m[PASS][0m testSetFeeToAbortDone() (gas: 425052)
[32m[PASS][0m testSetFeeToAbortDoneALL() (gas: 383501)
[32m[PASS][0m testSetFeeToOrderDone() (gas: 412054)
Test result: [32mok[0m. 4 passed; 0 failed; finished in 3.53ms

Running 1 test for test/foundry/multicall/Withdraw.t.sol:WithdrawMulticallTest
[32m[PASS][0m testFailMulticallWithdraw() (gas: 434883)
Test result: [32mok[0m. 1 passed; 0 failed; finished in 8.26ms

Running 8 tests for test/foundry/DeOrder/PayOrder.t.sol:PayOrder
[32m[PASS][0m testCannotPayOrder1() (gas: 131272)
[32m[PASS][0m testCannotPayOrder2() (gas: 183239)
[32m[PASS][0m testCannotPayOrder3() (gas: 26952)
[32m[PASS][0m testCannotPayOrder4() (gas: 131206)
[32m[PASS][0m testFailPayOrder3() (gas: 172646)
[32m[PASS][0m testFailPayOrder5() (gas: 177402)
[32m[PASS][0m testPayOrder() (gas: 291393)
[32m[PASS][0m testPayOrderWithPermit2() (gas: 378632)
Test result: [32mok[0m. 8 passed; 0 failed; finished in 9.35ms

Running 1 test for test/foundry/Permit2.t.sol:Permit2Test
[32m[PASS][0m testPermitTransferFrom() (gas: 97577)
Test result: [32mok[0m. 1 passed; 0 failed; finished in 943.79µs

Running 3 tests for test/foundry/DeOrder/ModifyOrder.t.sol:ModifyOrder
[32m[PASS][0m testCannotModifyOrder() (gas: 330126)
[32m[PASS][0m testModifyOrder() (gas: 264384)
[32m[PASS][0m testModifyOrderNotPay() (gas: 176855)
Test result: [32mok[0m. 3 passed; 0 failed; finished in 2.43ms

Running 2 tests for test/foundry/DeOrder/CreateOrder.t.sol:CreateOrder
[32m[PASS][0m testCannotCreateOrder() (gas: 23124)
[32m[PASS][0m testCreateOrder() (gas: 197305)
Test result: [32mok[0m. 2 passed; 0 failed; finished in 5.11ms

Running 2 tests for test/foundry/DeOrder/AppendStage.t.sol:AppendStage
[32m[PASS][0m testAppendStage() (gas: 384816)
[32m[PASS][0m testCannotAppendStage() (gas: 436924)
Test result: [32mok[0m. 2 passed; 0 failed; finished in 11.95ms

Running 1 test for test/foundry/DeOrder/OrderDone.t.sol:OrderDoneTest
[32m[PASS][0m testDoneOrder() (gas: 382411)
Test result: [32mok[0m. 1 passed; 0 failed; finished in 1.97ms

Running 1 test for test/foundry/BitMap.t.sol:BitMapTest
[32m[PASS][0m testBitMap() (gas: 42805)
Test result: [32mok[0m. 1 passed; 0 failed; finished in 279.75µs

Running 5 tests for test/foundry/DeOrder/confirmDelivery.sol:confirmDelivery
[32m[PASS][0m testConfirm() (gas: 419146)
[32m[PASS][0m testConfirmAppendStage() (gas: 539029)
[32m[PASS][0m testDue() (gas: 444092)
[32m[PASS][0m testDueAppendStage() (gas: 547405)
[32m[PASS][0m testfailzero() (gas: 315664)
Test result: [32mok[0m. 5 passed; 0 failed; finished in 6.16ms

Running 2 tests for test/foundry/DeOrder/StartOrder.t.sol:StartOrder
[32m[PASS][0m testCannotStartOrder() (gas: 280571)
[32m[PASS][0m testStartOrder() (gas: 324205)
Test result: [32mok[0m. 2 passed; 0 failed; finished in 5.09ms

Running 6 tests for test/foundry/attack/Attack.t.sol:AttackTest
[32m[PASS][0m testFailAttackAbortOrder() (gas: 391946)
[32m[PASS][0m testFailAttackModifyOrder() (gas: 258662)
[32m[PASS][0m testFailAttackMulticallWithdraw() (gas: 417261)
[32m[PASS][0m testFailAttackRefund() (gas: 258750)
[32m[PASS][0m testFailAttackTransfer() (gas: 218352)
[32m[PASS][0m testFailAttackWithdraw() (gas: 418943)
Test result: [32mok[0m. 6 passed; 0 failed; finished in 5.18ms

Running 4 tests for test/foundry/multicall/multicall.t.sol:MulticallTest
[32m[PASS][0m testMulticallPayOrderWithToken() (gas: 240167)
[32m[PASS][0m testMulticallPayOrderWithTokenAndZero() (gas: 233946)
[32m[PASS][0m testMulticallPayOrderWithZero() (gas: 179539)
[32m[PASS][0m testMulticallWithCreateOrder() (gas: 202606)
Test result: [32mok[0m. 4 passed; 0 failed; finished in 3.24ms

Running 5 tests for test/foundry/DeOrder/PermitStage.t.sol:PermitStage
[32m[PASS][0m testCannotPermitStage() (gas: 561979)
[32m[PASS][0m testCannotPermitStageWithArrayErr() (gas: 199671)
[32m[PASS][0m testCannotPermitStageWithErrNonce() (gas: 275703)
[32m[PASS][0m testPermitStage() (gas: 250028)
[32m[PASS][0m testPermitStage2() (gas: 250293)
Test result: [32mok[0m. 5 passed; 0 failed; finished in 8.42ms

Running 24 tests for test/foundry/DeTask.t.sol:DeTaskTest
[32m[PASS][0m testApplyAndCancel() (gas: 381727)
[32m[PASS][0m testApplyFor() (gas: 209717)
[32m[PASS][0m testApplyForTaskIdNotExist() (gas: 187459)
[32m[PASS][0m testCancelApply() (gas: 193433)
[32m[PASS][0m testCancelApplyTaskIdNotExist() (gas: 214794)
[32m[PASS][0m testCannotApplyAndCancel() (gas: 408994)
[32m[PASS][0m testCannotApplyFor() (gas: 404235)
[32m[PASS][0m testCannotCancelApply() (gas: 213908)
[32m[PASS][0m testCannotDisableTask() (gas: 184429)
[32m[PASS][0m testCannotModifyTaskNotIssuer() (gas: 193369)
[32m[PASS][0m testCannotSetMetaContract() (gas: 18273)
[32m[PASS][0m testCannotUpdateFeeReceiver() (gas: 13700)
[32m[PASS][0m testCreateTask() (gas: 178602)
[32m[PASS][0m testCreateTaskByDifferentPerson() (gas: 422814)
[32m[PASS][0m testDisableTask() (gas: 187810)
[32m[PASS][0m testFailApplyForApplicantNotExist() (gas: 208541)
[32m[PASS][0m testFailApplyForCostNotEnought() (gas: 190803)
[32m[PASS][0m testGetTaskInfoUseNotExistTaskId() (gas: 200712)
[32m[PASS][0m testModifyTask() (gas: 211941)
[32m[PASS][0m testModifyTaskUseTaskIdNotExist() (gas: 195703)
[32m[PASS][0m testSetMetaContract() (gas: 36927)
[32m[PASS][0m testTransferFee() (gas: 5520)
[32m[PASS][0m testUpdateFeeReceiver() (gas: 61605)
[32m[PASS][0m testUpdateFeeReceiverNotOwner() (gas: 16404)
Test result: [32mok[0m. 24 passed; 0 failed; finished in 7.61ms

Running 8 tests for test/foundry/DeOrder/Refund.t.sol:Refund
[32m[PASS][0m testConfirmIssuerAbortOrderrefund() (gas: 350236)
[32m[PASS][0m testConfirmRefundByTimeOutGetNormal() (gas: 669128)
[32m[PASS][0m testDueRefundByTimeOutGetNormal() (gas: 628533)
[32m[PASS][0m testDueissuerAbortOrderrefund() (gas: 408911)
[32m[PASS][0m testFailDueRefundByTimeOutGetNormal() (gas: 259772)
[32m[PASS][0m testRefundGreaterOrder() (gas: 392101)
[32m[PASS][0m testRefundNotStartOrder() (gas: 168619)
[32m[PASS][0m testRefundNotStartOrder2() (gas: 169015)
Test result: [32mok[0m. 8 passed; 0 failed; finished in 15.35ms

Running 22 tests for test/foundry/DeOrder/AbortOrder.t.sol:AbortOrder
[32m[PASS][0m testAbortOrder() (gas: 360084)
[32m[PASS][0m testCannotAbortOrder() (gas: 324524)
[32m[PASS][0m testCannotConfirmIusserAbortOrder() (gas: 312468)
[32m[PASS][0m testCannotConfirmWorkerAbortOrder() (gas: 312849)
[32m[PASS][0m testCannotDueIusserAbortOrder() (gas: 371811)
[32m[PASS][0m testCannotDueWorkerAbortOrder() (gas: 312662)
[32m[PASS][0m testConfirmLongtime() (gas: 337513)
[32m[PASS][0m testDueLongtime() (gas: 323166)
[32m[PASS][0m testMorDueIssuererAppendStageWorkerAbortOrder() (gas: 472598)
[32m[PASS][0m testMoreConfirmIssuerAppendStageIssuerAbortOrder() (gas: 487047)
[32m[PASS][0m testMoreConfirmIusserAbortOrder() (gas: 510451)
[32m[PASS][0m testMoreConfirmWorkerAbortOrder() (gas: 509996)
[32m[PASS][0m testMoreConfirmWorkerAppendStageIssuerAbortOrder() (gas: 509272)
[32m[PASS][0m testMoreConfirmdIssuererAppendStageWorkerAbortOrder() (gas: 486239)
[32m[PASS][0m testMoreDueIssuerAppendStageIssuerAbortOrder() (gas: 473546)
[32m[PASS][0m testMoreDueIusserAbortOrder() (gas: 491162)
[32m[PASS][0m testMoreDueWorkerAbortOrder() (gas: 489970)
[32m[PASS][0m testMoreDueWorkerAppendStageIssuerAbortOrder() (gas: 495857)
[32m[PASS][0m testprolongStageConfirmIssuerAbortOrder() (gas: 327802)
[32m[PASS][0m testprolongStageConfirmWorkerAbortOrder() (gas: 350340)
[32m[PASS][0m testprolongStageDueIssuerAbortOrder() (gas: 387459)
[32m[PASS][0m testprolongStageDueWorkerAbortOrder() (gas: 350247)
Test result: [32mok[0m. 22 passed; 0 failed; finished in 18.91ms
| contracts/DeOrder.sol:DeOrder contract |                 |       |        |        |         |
|----------------------------------------|-----------------|-------|--------|--------|---------|
| Deployment Cost                        | Deployment Size |       |        |        |         |
| 3298025                                | 16288           |       |        |        |         |
| Function Name                          | min             | avg   | median | max    | # calls |
| DOMAIN_SEPARATOR                       | 445             | 1629  | 2445   | 2445   | 103     |
| PERMITAPPENDSTAGE_TYPEHASH             | 276             | 276   | 276    | 276    | 18      |
| PERMITPROSTAGE_TYPEHASH                | 320             | 320   | 320    | 320    | 15      |
| PERMITSTAGE_TYPEHASH                   | 804             | 804   | 804    | 804    | 70      |
| abortOrder                             | 718             | 41037 | 28972  | 92448  | 34      |
| appendStage                            | 1268            | 28026 | 32353  | 52311  | 18      |
| builderSBT                             | 711             | 711   | 711    | 711    | 1       |
| confirmDelivery                        | 1193            | 2849  | 1389   | 7627   | 48      |
| createOrder                            | 746             | 90892 | 99129  | 117029 | 91      |
| currOrderId                            | 731             | 731   | 731    | 731    | 1       |
| fee                                    | 973             | 1830  | 973    | 2973   | 7       |
| feeTo                                  | 315             | 1172  | 315    | 2315   | 7       |
| getOrder                               | 2598            | 2598  | 2598   | 2598   | 21      |
| getStages                              | 2235            | 2764  | 2853   | 3472   | 7       |
| issuerSBT                              | 1019            | 1019  | 1019   | 1019   | 1       |
| modifyOrder                            | 958             | 9255  | 4180   | 33876  | 23      |
| multicall                              | 2850            | 52707 | 45120  | 178060 | 9       |
| nonces                                 | 769             | 2197  | 2769   | 2769   | 98      |
| owner                                  | 799             | 799   | 799    | 799    | 1       |
| payOrder                               | 6007            | 28035 | 37808  | 37808  | 103     |
| payOrderWithPermit2                    | 64394           | 64394 | 64394  | 64394  | 1       |
| permitStage                            | 2471            | 98432 | 98185  | 147728 | 70      |
| prolongStage                           | 1436            | 11630 | 9315   | 29245  | 15      |
| receive                                | 125             | 125   | 125    | 125    | 107     |
| refund                                 | 1362            | 6286  | 2481   | 24204  | 64      |
| setFeeTo                               | 2661            | 8132  | 9843   | 13943  | 6       |
| setSBT                                 | 2895            | 25005 | 25005  | 47115  | 2       |
| setSupportToken                        | 2606            | 23740 | 26054  | 26054  | 11      |
| startOrder                             | 917             | 4565  | 4444   | 5408   | 57      |
| supportTokens                          | 913             | 1913  | 1913   | 2913   | 2       |
| transferOwnership                      | 3309            | 5569  | 5569   | 7830   | 2       |
| updateAttachment                       | 1321            | 2860  | 2400   | 5321   | 4       |
| withdraw                               | 449             | 17859 | 5554   | 81778  | 72      |


| contracts/DeTask.sol:DeTask contract |                 |        |        |        |         |
|--------------------------------------|-----------------|--------|--------|--------|---------|
| Deployment Cost                      | Deployment Size |        |        |        |         |
| 1672756                              | 8756            |        |        |        |         |
| Function Name                        | min             | avg    | median | max    | # calls |
| applyAndCancel                       | 2198            | 23279  | 19620  | 51681  | 4       |
| applyFor                             | 692             | 15485  | 17196  | 27146  | 10      |
| cancelApply                          | 2104            | 2754   | 3080   | 3080   | 3       |
| createTask                           | 102557          | 139352 | 148357 | 148357 | 23      |
| disableTask                          | 868             | 1577   | 1095   | 2768   | 3       |
| getTaskInfo                          | 3017            | 3017   | 3017   | 3017   | 29      |
| meta                                 | 766             | 766    | 766    | 766    | 1       |
| modifyTask                           | 2521            | 7228   | 7715   | 10963  | 4       |
| setMetaContract                      | 2509            | 9894   | 2564   | 24609  | 3       |
| updateFeeReceiver                    | 2804            | 33714  | 48645  | 50745  | 6       |


| contracts/mock/WETH.sol:WETH contract |                 |       |        |       |         |
|---------------------------------------|-----------------|-------|--------|-------|---------|
| Deployment Cost                       | Deployment Size |       |        |       |         |
| 440075                                | 2130            |       |        |       |         |
| Function Name                         | min             | avg   | median | max   | # calls |
| approve                               | 24310           | 24310 | 24310  | 24310 | 3       |
| balanceOf                             | 560             | 693   | 560    | 2560  | 15      |
| deposit                               | 0               | 17532 | 23999  | 23999 | 105     |
| totalSupply                           | 217             | 217   | 217    | 217   | 23      |
| transfer                              | 25106           | 25106 | 25106  | 25106 | 1       |
| transferFrom                          | 635             | 10265 | 3637   | 26006 | 8       |
| withdraw                              | 2430            | 8466  | 9144   | 9144  | 110     |


| lib/permit2/src/Permit2.sol:Permit2 contract |                 |       |        |       |         |
|----------------------------------------------|-----------------|-------|--------|-------|---------|
| Deployment Cost                              | Deployment Size |       |        |       |         |
| 1547293                                      | 7920            |       |        |       |         |
| Function Name                                | min             | avg   | median | max   | # calls |
| DOMAIN_SEPARATOR                             | 327             | 327   | 327    | 327   | 82      |
| permitTransferFrom                           | 56266           | 57516 | 57516  | 58766 | 2       |


| test/foundry/attack/AttackAbortOrder.sol:AttackAbortOrder contract |                 |        |        |        |         |
|--------------------------------------------------------------------|-----------------|--------|--------|--------|---------|
| Deployment Cost                                                    | Deployment Size |        |        |        |         |
| 315816                                                             | 1585            |        |        |        |         |
| Function Name                                                      | min             | avg    | median | max    | # calls |
| attack                                                             | 28698           | 28698  | 28698  | 28698  | 1       |
| receive                                                            | 3978            | 3978   | 3978   | 3978   | 1       |
| start                                                              | 183964          | 183964 | 183964 | 183964 | 1       |


| test/foundry/attack/AttackMulticallWithdraw.sol:AttackMulticallWithdraw contract |                 |        |        |        |         |
|----------------------------------------------------------------------------------|-----------------|--------|--------|--------|---------|
| Deployment Cost                                                                  | Deployment Size |        |        |        |         |
| 396691                                                                           | 1989            |        |        |        |         |
| Function Name                                                                    | min             | avg    | median | max    | # calls |
| attack                                                                           | 58504           | 58504  | 58504  | 58504  | 1       |
| receive                                                                          | 7728            | 7728   | 7728   | 7728   | 1       |
| start                                                                            | 104395          | 104395 | 104395 | 104395 | 1       |


| test/foundry/attack/AttackRefund.sol:AttackRefund contract |                 |        |        |        |         |
|------------------------------------------------------------|-----------------|--------|--------|--------|---------|
| Deployment Cost                                            | Deployment Size |        |        |        |         |
| 218924                                                     | 1101            |        |        |        |         |
| Function Name                                              | min             | avg    | median | max    | # calls |
| attack                                                     | 101439          | 101439 | 101439 | 101439 | 2       |
| receive                                                    | 4961            | 4961   | 4961   | 4961   | 2       |


| test/foundry/attack/AttackTransfer.t.sol:AttackTransfer contract |                 |      |        |      |         |
|------------------------------------------------------------------|-----------------|------|--------|------|---------|
| Deployment Cost                                                  | Deployment Size |      |        |      |         |
| 246148                                                           | 1237            |      |        |      |         |
| Function Name                                                    | min             | avg  | median | max  | # calls |
| attack                                                           | 6540            | 6540 | 6540   | 6540 | 1       |


| test/foundry/attack/AttackWithdraw.sol:AttackWithdraw contract |                 |        |        |        |         |
|----------------------------------------------------------------|-----------------|--------|--------|--------|---------|
| Deployment Cost                                                | Deployment Size |        |        |        |         |
| 257961                                                         | 1296            |        |        |        |         |
| Function Name                                                  | min             | avg    | median | max    | # calls |
| attack                                                         | 50536           | 50536  | 50536  | 50536  | 1       |
| receive                                                        | 3738            | 3738   | 3738   | 3738   | 1       |
| start                                                          | 104357          | 104357 | 104357 | 104357 | 1       |


| test/foundry/mock/MockERC20.sol:MockERC20 contract |                 |       |        |       |         |
|----------------------------------------------------|-----------------|-------|--------|-------|---------|
| Deployment Cost                                    | Deployment Size |       |        |       |         |
| 608931                                             | 4337            |       |        |       |         |
| Function Name                                      | min             | avg   | median | max   | # calls |
| approve                                            | 24310           | 24310 | 24310  | 24310 | 163     |
| balanceOf                                          | 582             | 1364  | 582    | 2582  | 23      |
| mint                                               | 46501           | 46501 | 46501  | 46501 | 82      |
| transfer                                           | 2312            | 2312  | 2312   | 2312  | 2       |
| transferFrom                                       | 2760            | 20180 | 27783  | 29783 | 9       |


| test/foundry/mock/mock.sol:Mock contract |                 |      |        |       |         |
|------------------------------------------|-----------------|------|--------|-------|---------|
| Deployment Cost                          | Deployment Size |      |        |       |         |
| 426371                                   | 2060            |      |        |       |         |
| Function Name                            | min             | avg  | median | max   | # calls |
| mockOneTask                              | 4646            | 5340 | 4646   | 10438 | 25      |



