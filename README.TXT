==readme==

Log analyser test work. It has one class LogAnalyser


Usage for this class:

analyser = LogAnalyser(path_to_logfile) #can raise LAFileNotFoundException if file does not exist
analyser.sended_by_email('mi_email@email.com') #return count sended emails
analyser.total_sended() #total sended
analyser.total_failed() #total failed

