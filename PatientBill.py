from unicodedata import name
import PatientClass as pc
import ProcedureClass as pd

def main():
    
    patient = pc.Patient('1','Matt Jones','123 Main st, Waco TX 76706','254-555-7415',True)
    phs = pd.Procedure('Physical Exam','2/15/2022','Dr. Irvine',250.00,'1')
    mri = pd.Procedure('MRI','2/15/2022','Dr. Hamilton',1500.00,'1')
    ct = pd.Procedure('CT Scan','2/17/2022','Dr. Drey','1200','2')
    
    print('*** Patient Bill***')
    patient.print_patient()
    phs.print_procedure()
    mri.print_procedure()

    print('Total Charges:', '$', 1500 + 250)
    
    

main()