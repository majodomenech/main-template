#!python3
import redflagbpm

bpm = redflagbpm.BPMService()
idProcessInstance = bpm.execution.getProcessInstanceId()
