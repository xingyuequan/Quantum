import cirq
import numpy as np
def quantum_state_helper(circuit):
  # Get the qubits involved in the circuit
  qubits = circuit.all_qubits()
  # Get the number of qubits
  n = len(qubits)
  # Create a simulator to run the circuit
  simulator = cirq.Simulator()
  # Get the final state vector of the circuit
  state_vector = simulator.simulate(circuit).final_state_vector
  # Convert the state vector to a ket vector
  ket_vector = cirq.dirac_notation(state_vector)
  # Convert the state vector to a density matrix
  density_matrix = np.outer(state_vector, np.conj(state_vector))
  # Print the ket vector and the density matrix
  print(circuit,ket_vector, density_matrix,sep='\n')

# 创建两个量子比特
q0 = cirq.NamedQubit('q0')
q1 = cirq.NamedQubit('q1')

# 创建一个量子电路
circuit = cirq.Circuit()

# 在第一个量子比特上施加一个X轴旋转门，角度为π/2
circuit.append(cirq.X(q0)**0.5)
quantum_state_helper(circuit)
# 在两个量子比特上施加一个CNOT门
circuit.append(cirq.CNOT(q0, q1))

# 在两个量子比特上施加测量门，并命名为'm'
circuit.append(cirq.measure(q0, q1, key='m'))

# 打印电路图
print('Circuit:')
print(circuit)

# 创建一个模拟器
simulator = cirq.Simulator()

# 运行电路100次，得到测量结果
result = simulator.run(circuit, repetitions=100)

# 打印测量结果的直方图
print('Histogram of results:')
print(result.histogram(key='m'))